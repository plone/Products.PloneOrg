
import transaction
from AccessControl.SpecialUsers import system
from AccessControl.SecurityManagement import newSecurityManager
from Products.CMFCore.utils import getToolByName
from Testing.makerequest import makerequest
from Products.CMFCore.utils import getToolByName

app=makerequest(app)
acl_users = app.acl_users
user = acl_users.getUser('admin')
user = user.__of__(acl_users)
#newSecurityManager(None, system)
newSecurityManager(None, user)
portal = app['plone.org']
wf = getToolByName(portal, 'portal_workflow')

#items = portal.ZopeFind(portal, obj_metatypes=['PoiTracker',], search_sub=1)
#for obj in items:

brains = portal.portal_catalog(portal_type='PoiPscTracker',path='plone.org')
for brain in brains:
    count = 0
    obj = brain.getObject()
    print '%s' % '/'.join(obj.getPhysicalPath())
    review_state = wf.getInfoFor(obj, 'review_state')
    if not review_state == 'restricted': 
        if review_state == 'open' or review_state == 'close':
            wf.doActionFor(obj,'restrict',wf_id='poi_tracker_workflow')
            count += 1
            print '    Restricting tracker: %s' % '/'.join(obj.getPhysicalPath())
            if count % 25 == 0:
                transaction.commit()
                print '    (Committed)'
transaction.commit()
print '    (Committed, final.)'


