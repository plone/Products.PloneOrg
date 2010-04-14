import getopt
import sys
import logging
import transaction
import AccessControl
from itertools import izip
from ZODB.POSException import ConflictError
from Testing.makerequest import makerequest
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.log import log, log_exc, logger
from Products.CMFPlone.utils import base_hasattr, safe_callable

THRESHOLD = 100

class ContentUpdater(object):
    """Performs actions on ZODB objects using a catalog search or ZopeFind,
    commits full transactions on batches to avoid conflicts"""

    def __init__(self, context):
        self.context = context
        self._catalog = getToolByName(context, 'portal_catalog')
        self._uid_catalog = getToolByName(context, 'uid_catalog')

    def conflict_safe_catalog_update(self, query, action, threshold,
                                     res_filter=None):
        """Performs an action on objects found with a catalog query
        in a way that tries to minimize conflicts"""
        cat = self._catalog
        brains = cat(query)
        total = len(brains)
        if res_filter is None:
            res_filter = lambda x: True
        # split into filtered sub-lists of size threshold before filtering
        slices = ((o for o in brains[start:end] if res_filter(o))
                    for start, end in izip(xrange(0, total, threshold),
                               xrange(threshold, total+threshold, threshold)))
        # Run an abort here to help avoid conflicts on the first batch
        # resulting from the extended catalog search
        transaction.abort()
        log('Transaction abort after finding all content (%s objects)'%total)
        self.context._p_jar.sync()
        return self._conflict_safe_update(slices, action)

    def conflict_safe_find_and_update(self, action, threshold, res_filter=None,
                                      **kw):
        """Find objects with ZopeFind and perform actions on them
        in batches.  Takes the same keyword args as ZopeFind"""
        results = self.context.ZopeFind(self.context, search_sub=True, **kw)
        total = len(results)
        if res_filter is None:
            res_filter = lambda x: True
        # Split the results into subsets lazily
        slices = ((o for (p, o) in results[start:end] if res_filter(o))
                  for start, end in izip(xrange(0, total, threshold),
                                 xrange(threshold, total+threshold, threshold)))
        # Run an abort here to help avoid conflicts on the first batch
        # resulting from the extended run of ZopeFind
        transaction.abort()
        log('Transaction abort after finding all content (%s objects).'%total)
        self.context._p_jar.sync()
        return self._conflict_safe_update(slices, action)

    def _conflict_safe_update(self, slices, action):
        """Perform an action on groups of objects, with transaction
        commits along the way"""
        updated = []
        trans_failed = []
        commit = transaction.commit
        sync = self.context._p_jar.sync
        obj_path = self._obj_path
        for n,s in enumerate(slices):
            # skip cache purging
            resolved = list(s)
            if not resolved:
                #log('Batch %s was empty'%n)
                continue
            [action(r) for r in resolved]
            try:
                commit()
                log('Full transaction committed on batch %s (%s) '%(n,
                                                                 len(resolved)))
                sync()
            except ConflictError:
                transaction.abort()
                log('Conflict on batch %s, retrying ...'% n,
                    severity=logging.WARN)
                # try once more
                [action(r) for r in resolved]
                try:
                    commit()
                    log('Full transaction committed after retry on batch %s'% n,
                        severity=logging.WARN)
                    sync()
                except ConflictError:
                    transaction.abort()
                    log_exc('Conflict after two tries on batch %s, continuing'%n)
                    trans_failed.extend(obj_path(o) for o in resolved)
                    continue
            updated.extend(obj_path(o) for o in resolved)
        return updated, trans_failed

    @staticmethod
    def _obj_path(obj):
        if hasattr(obj, 'getPath'):
            return obj.getPath()
        return '/'.join(obj.getPhysicalPath())

    @staticmethod
    def _indexObject(obj):
        if (base_hasattr(obj, 'getObject') and
            safe_callable(obj.getObject)):
            # Wake up any brains
            obj = obj.getObject()
        if (base_hasattr(obj, 'indexObject') and
            safe_callable(obj.indexObject)):
            try:
                obj.indexObject()
            except TypeError:
                # Catalogs have 'indexObject' as well, but they
                # take different args, and will fail
                pass
            except:
                # Log indexing exceptions but continue
                log_exc('Could not reindex %s'%(
                    '/'.join(obj.getPhysicalPath())))

    def reindexCatalog(self, threshold=THRESHOLD):
        """Find every object in the catalog and reindex"""
        return self.conflict_safe_catalog_update({}, self._indexObject,
                                                 threshold=threshold)

    def findAndIndexAll(self, threshold=THRESHOLD):
        """Finds all content with an indexObject method and indexes"""
        return self.conflict_safe_find_and_update(self._indexObject,
                                                  threshold=threshold,
                        # DTML ugliness
                        obj_expr='_.hasattr(this().aq_explicit, "indexObject")')

    def clearAndRebuildCatalog(self, threshold=THRESHOLD):
        """Erases the catalog, then finds everything and indexes it.
        This is dangerous because an uncaught exception in the middle
        can result in an incomplete catalog.  Additionally, at any
        given time during the run of this script the catalogs will be
        in an incomplete state."""
        self._catalog.manage_catalogClear()
        self._uid_catalog.manage_catalogClear()
        transaction.commit()
        log('Full transaction after emptying catalogs. '
            'The site may be broken at this point')
        return self.findAndIndexAll(threshold)


class RebuildScript(object):

    def __init__(self, build_type='find', site_id='plone.org',
                 threshold=THRESHOLD):
        self.build_type = build_type
        self.site_id = site_id
        self.threshold = threshold

    def usage(self):
        print """
This script will reindex the catalog of your plone site.  By default
it will look for a site with id 'plone.org' and will simply index all
indexale objects in the portal.  Other indexing options are available:

    -s, --site=: Choose an alternative id for your plone site
    -t, --type=: Select the type of reindex to perform.  The following types
                 are available:

                   find:   Indexes all indexable content in the portal (default)
                   reindex:Reindexes all content already indexed
                   clear:  Clears the catalog and then indexes all indexable
                           content.  ***This is potentially dangerous as it
                           will place the catalog in an inconsistent state
                           while running***
    -h, --help:  Prints this message to stdout.
"""

    def arg_handler(self):
        try:
            opts, args = getopt.getopt(sys.argv[1:], 'ht:s:',
                                       ['help', 'type=','site='])
        except getopt.GetoptError:
            self.usage()
            sys.exit(2)
        for opt, arg in opts:
            if opt in ('-h', '--help'):
                self.usage()
                sys.exit()
            elif opt in ('-t', '--type'):
                self.build_type = arg
                if self.build_type == 'clear':
                    resp = raw_input('This will temporarily break the site '
                                     'while rebuilding the catalog?  Are you '
                                     'sure you want to continue (y/n)?')
                    if resp.strip() != 'y':
                        sys.exit()
            elif opt in ('-s', '--site'):
                self.site_id = arg

    def run(self, app):
        self.arg_handler()
        AccessControl.SecurityManagement.newSecurityManager(None,
                                              AccessControl.SpecialUsers.system)
        app=makerequest(app)
        indexer = ContentUpdater(app[self.site_id])
        indexers = {'reindex': indexer.reindexCatalog,
                    'find': indexer.findAndIndexAll,
                    'clear': indexer.clearAndRebuildCatalog}
        updated, failed = indexers[self.build_type](threshold=self.threshold)
        print "Reindexed %s objects"%len(updated)
        if failed:
            print "ConflictErrors prevented reindex of %s objects"%len(failed)

if __name__ == '__main__':
    # log everything to stderr
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())
    # app should be defined if running from zopepy or zopectl run
    RebuildScript().run(app)
