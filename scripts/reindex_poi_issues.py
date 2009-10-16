brains = context.portal_catalog.searchResults(portal_type='PoiIssue')
for brain in brains:
    brain.getObject().reindexObject()
