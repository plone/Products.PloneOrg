from Products.CMFCore.utils import getToolByName
from StringIO import StringIO
import transaction

from AccessControl.SecurityManagement import newSecurityManager
from AccessControl.SecurityManager import setSecurityPolicy
from Testing.makerequest import makerequest
from Products.CMFCore.tests.base.security import PermissiveSecurityPolicy, OmnipotentUser
_policy=PermissiveSecurityPolicy()
_oldpolicy=setSecurityPolicy(_policy)
newSecurityManager(None, OmnipotentUser().__of__(app.acl_users))
app=makerequest(app)
attool = app['plone.org'].archetype_tool

def manage_updateSchema(self, REQUEST=None, update_all=None,
                        remove_instance_schemas=None):
    """Make sure all objects' schema are up to date.
    """
    out = StringIO()
    print >> out, 'Updating schema...'

    update_types = []
    if REQUEST is None:
        # DM (avoid persistency bug): avoid code duplication
        update_types = [ti[0] for ti in self.getChangedSchema() if ti[1]]
    else:
        # DM (avoid persistency bug):
        update_types = [ti[0] for ti in self.getChangedSchema() if ti[1]]
        update_all = REQUEST.form.get('update_all', False)
        remove_instance_schemas = REQUEST.form.get(
            'remove_instance_schemas', remove_instance_schemas)

    # XXX: Enter this block only when there are types to update!
    if update_types:
        # Use the catalog's ZopeFindAndApply method to walk through
        # all objects in the portal.  This works much better than
        # relying on the catalog to find objects, because an object
        # may be uncatalogable because of its schema, and then you
        # can't update it if you require that it be in the catalog.
        catalog = getToolByName(self, 'portal_catalog')
        portal = getToolByName(self, 'portal_url').getPortalObject()
        for t in self.listRegisteredTypes():
            ident = "%s.%s"%(t['package'],t['name'])
            if ident not in update_types:
                continue            
            meta_type = t['meta_type']
#            if meta_type == "PSCFile":
#                continue
            if meta_type == "PSCProject":
                if remove_instance_schemas:
                    print "I'll remove the schema too"
                    func_update_changed = self._removeSchemaAndUpdateChangedObject
                    func_update_all = self._removeSchemaAndUpdateObject
                else:
                    func_update_changed = self._updateChangedObject
                    func_update_all = self._updateObject
                if update_all:
                    catalog.ZopeFindAndApply(portal, obj_metatypes=(meta_type,),
                        search_sub=True, apply_func=func_update_all)
                else:
                    print "Updating %s" % t
                    catalog.ZopeFindAndApply(portal, obj_metatypes=(meta_type,),
                        search_sub=True, apply_func=func_update_changed)
                print "Updating signature of %s" % (t['meta_type'])
                print "Signature %s is changing to %s" % (`self._types[ident]`, `t['signature']`)
                self._types[ident] = t['signature']
                self._p_changed = True
                transaction.commit()

            else:
                print "Doing nothing with %s" % meta_type

    print >> out, 'Done.'
    return out.getvalue()

print manage_updateSchema(attool, REQUEST=app.REQUEST, remove_instance_schemas=True)
transaction.commit()

