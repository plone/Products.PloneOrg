## Script (Python) "kupu_document_write"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=data
##title=support for new.plone.org - waiting for new kupu release
##
print '<script type="text/javascript">'
quoted = "<', '".join(data.replace(r"'", r"\'").split('<'))
lines = quoted.split('\n')
print "    document.write('%s');" % "', '".join(lines)
print "</script>"
return printed
