## Script (Python) "davisagli_reindex_plips"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
n = 0
roadmaps = context.portal_catalog.searchResults(portal_type='PSCImprovementProposalFolder')
for roadmap in roadmaps:
    for plip in roadmap.getObject().objectValues():
        if not context.portal_catalog.searchResults(UID=plip.UID()):
            plip.reindexObject()
            n += 1
print n
return printed
