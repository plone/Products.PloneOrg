# kupu can accumulate bad type info in its linkable resource list

klt = context.kupu_library_tool
ptypes = klt.getPortalTypesForResourceType('linkable')

all_portal_types = dict([ (t.id, 1) for t in context.portal_types.listTypeInfo()])

portal_types = [ptype.strip() for ptype in ptypes if ptype]

print "bad types: ",
print [p for p in portal_types if p not in all_portal_types]

ok_types = [p for p in portal_types if p in all_portal_types]
print "OK types:", ok_types

klt.updateResourceTypes(({'resource_type' : 'linkable',
                          'old_type'      : 'linkable',
                          'portal_types'  :  ok_types},))

return printed
