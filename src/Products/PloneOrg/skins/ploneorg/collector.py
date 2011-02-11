## Script (Python) "collector"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Redirect for the old Collector
##
request = context.REQUEST
response = request.RESPONSE
url = 'http://dev.plone.org/plone/'
if traverse_subpath and traverse_subpath[0].isdigit():
    url += '/'.join(['ticket',]+traverse_subpath)
else:
    url += 'report/1'
return response.redirect(url)