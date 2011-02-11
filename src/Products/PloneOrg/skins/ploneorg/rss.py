## Script (Python) "rss"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Redirect for the old RSS feed
##
request = context.REQUEST
response = request.RESPONSE
if traverse_subpath and traverse_subpath[0]=='RSSTopic':
    return response.redirect('/news/newslisting/RSS')
raise "NotFound"