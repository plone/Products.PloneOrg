
import transaction
from AccessControl.SpecialUsers import system
from AccessControl.SecurityManagement import newSecurityManager
from Products.CMFCore.utils import getToolByName
from Testing.makerequest import makerequest
from Products.CMFCore.utils import getToolByName

app=makerequest(app)
newSecurityManager(None, system)
portal = app['plone.org']
wf = getToolByName(portal, 'portal_workflow')

#brains = portal.portal_catalog(portal_type='PoiTracker',path='plone.org')
#for brain in brains:
#    obj = brain.getObject()


items = portal.ZopeFind(portal, obj_metatypes=['PoiTracker',], search_sub=1)
for obj in items:
    print '%s' % '/'.join(obj[1].getPhysicalPath())






#    review_state = wf.getInfoFor(obj, 'review_state')
#    if not review_state == 'restricted':
#        wf.doActionFor(obj,'restrict',wf_id='poi_workflow')
#        print '    Restricting tracker: %s' %
#            '/' + '/'.join(portal.getPhysicalPath(obj))
