import transaction
from AccessControl.SpecialUsers import system
from AccessControl.SecurityManagement import newSecurityManager
from Products.CMFCore.utils import getToolByName
from Testing.makerequest import makerequest

app=makerequest(app)
newSecurityManager(None, system)

portal = app['plone.org']

utool = portal.portal_url
brains = portal.portal_catalog.searchResults(portal_type='PSCRelease', path='/plone.org/products')
for brain in brains:
    obj = brain.getObject()
    path = '/' + '/'.join(utool.getRelativeContentPath(obj))
    print 'Reindexing %s' % path
    obj.reindexObject(['getCategories', 'getClassifiers', 'getCompatibility'])
