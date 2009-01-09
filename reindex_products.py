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
count = 0
for brain in brains:
    count += 1
    obj = brain.getObject()
    path = '/' + '/'.join(utool.getRelativeContentPath(obj))
    print 'Reindexing %s' % path
    obj.reindexObject(['getCategories', 'getClassifiers', 'getCompatibility'])
    if count % 10 == 0:
        print 'Committing...'
        transaction.commit()
        print 'Done.'
    
