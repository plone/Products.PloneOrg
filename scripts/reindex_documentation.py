log = context.portal_catalog
brains = catalog.searchResults(portal_type=('HelpCenter', 'PSCDocumentationFolder'))
for brain in brains:
    if brain.getURL() == 'http://new.plone.org:8080/plone.org/documentation':
        continue
    print brain.getURL()

    obj = brain.getObject()
    items = catalog.searchResults(path='/'.join(obj.getPhysicalPath()))
    for item in items:
        item.getObject().reindexObject()
return printed
