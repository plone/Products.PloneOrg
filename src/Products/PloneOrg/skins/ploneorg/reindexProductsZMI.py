## parameters=start,stop

start = int(start)
stop = int(stop)

results = container.portal_catalog(portal_type='PSCProject')
print "Processing %s Records"%len(results)
if stop > len(results):
    stop = len(results) - 1
if start > stop:
    return 
errors = []
for result in results[start:stop]:
      try:
           obj = result.getObject()
           obj.reindexObject()
           print "Reindexed %s"%obj.absolute_url()
      except:
           errors.append(obj.absolute_url())
if len(errors):
    print "ERRORS: "
for error in errors:
    print error
return printed
