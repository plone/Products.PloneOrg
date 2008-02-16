from Products.CMFCore.DirectoryView import registerDirectory
from Products.CMFCore.DirectoryView import registerFileExtension
from Products.CMFCore.FSFile import FSFile
from Products.ATContentTypes.permission import permissions

from Products.PloneOrg.config import *
#import Products.PloneOrg.content

registerDirectory("skins", GLOBALS)
registerFileExtension("zip", FSFile)
registerFileExtension("txt", FSFile)

# def initialize(context):
#     listOfTypes = listTypes(PROJECTNAME)
#     (content_types, constructors, ftis) = \
#             process_types(listOfTypes, PROJECTNAME)
# 
# 
#     allTypes = zip(content_types, constructors)
#     for atype, constructor in allTypes:
#         kind = "%s: %s" % (PROJECTNAME, atype.archetype_name)
#         ContentInit(
#                 kind,
#                 content_types      = (atype,),
#                 permission         = permissions[atype.portal_type],
#                 extra_constructors = (constructor,),
#                 ).initialize(context)
# 
# 
# 
