## Script (Python) "reindex_products"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
brains = context.portal_catalog.searchResults(portal_type='PSCRelease', path='/plone.org/products')
for brain in brains:
    obj = brain.getObject()
    obj.reindexObject(['getCategories', 'getClassifiers', 'getCompatibility'])
    print obj.getId()

return printed
