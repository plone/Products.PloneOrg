## Script (Python) "reindex_poi_issues"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
brains = context.portal_catalog.searchResults(portal_type='PoiIssue')
for brain in brains:
    brain.getObject().reindexObject()
