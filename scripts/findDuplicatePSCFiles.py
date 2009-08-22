import transaction
from AccessControl.SpecialUsers import system
from AccessControl.SecurityManagement import newSecurityManager
from Products.CMFCore.utils import getToolByName
from Testing.makerequest import makerequest

app=makerequest(app)
newSecurityManager(None, system)

portal = app['plone.org']

utool = portal.portal_url
brains = portal.portal_catalog.searchResults(portal_type='PSCFile', path='plone.org/products')
count = 0

#17:59 < tarek> brain.getObject().getId()
#17:59 < tarek> and build a dict
#17:59 < tarek> wth the ids as keys,
#17:59 < tarek> using a defaultdict or something
#18:00 < tarek> if it doesn exist -> dict[key] = [package]
#18:00 < tarek> if it exists dict[key].append(package2)
#18:00 < tarek> and all the keys with len > 1 are the bad guys :D
for brain in brains:
    count += 1
    obj = brain.getObject()
    path = '/' + '/'.join(utool.getRelativeContentPath(obj))
    print 'I found %s' % path
