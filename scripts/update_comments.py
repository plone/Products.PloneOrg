"""
Script to update cooked comments
"""

SITE = 'plone.org'
try:
    import readline
except ImportError:
    print "Module readline not available."
else:
    import rlcompleter
    readline.parse_and_bind("tab: complete")


import transaction, pdb
from zope.interface import implementedBy
from zope.component import getUtility, queryUtility, queryAdapter
from Zope2 import debug
from Acquisition import aq_inner, aq_parent, aq_chain, aq_base
from zope.app.component.hooks import setSite, getSiteManager
from Testing.makerequest import makerequest
from AccessControl.SecurityManagement import newSecurityManager, getSecurityManager

app = makerequest(app)
site = app.unrestrictedTraverse(SITE)
setSite(site)
user = app.acl_users.getUser('admin').__of__(site.acl_users)
newSecurityManager(None, user)

content = site.portal_catalog.unrestrictedSearchResults()
commented = []
for brain in content:
    ob = brain.getObject()
    tb = getattr(ob.aq_base, 'talkback', None)
    if tb is not None:
        commented.append(ob)

from plone.intelligenttext.transforms import convertWebIntelligentPlainTextToHtml
dis = [di for item in commented for di in item.talkback._container.values()]

bad_dis = [di for di in dis if convertWebIntelligentPlainTextToHtml(di.text) != di.cooked_text]

for di in bad_dis:
    di.cooked_text = convertWebIntelligentPlainTextToHtml(di.text)

print "%s content items, %s commented upon, %s comments, %s updated." % (len(content), len(commented), len(dis), len(bad_dis))

import sys
if sys.argv[-1] == 'commit':
    transaction.commit()
    print 'Transaction committed.'
else:
    transaction.abort()
    print "Transaction aborted, you may pass 'commit' as an argument to this script."
