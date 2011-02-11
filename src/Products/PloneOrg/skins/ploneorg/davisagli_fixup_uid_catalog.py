## Script (Python) "davisagli_fixup_uid_catalog"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
uids = [r.targetUID for r in context.reference_catalog() if not context.uid_catalog(UID=r.targetUID)]

found = []
notfound = []
for uid in uids:
  res = context.portal_catalog(UID=uid)
  if res:
    found.append(uid)
    o = res[0].getObject()
    url = '/'.join(o.getPhysicalPath()[2:])
    context.uid_catalog.catalog_object(o, url)
  else:
    # XXX figure out how to clean up references that are really broken
    notfound.append(uid)

print "%s found: %s" % (len(found), list(found))
print "%s notfound: %s" % (len(notfound), list(notfound))
return printed
