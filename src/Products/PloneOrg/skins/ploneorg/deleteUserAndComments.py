## Script (Python) "deleteUserAndComments"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=memberid
##title=
##
if context.REQUEST.get('REQUEST_METHOD', 'GET').upper() != 'POST':
    raise 'Forbidden'

portal = context.portal_url.getPortalObject()

brains = portal.portal_catalog(portal_type="Discussion Item", Creator=memberid)

countSuccess = 0
countFail = 0

for brain in brains:
    comment = brain.getObject()
    traversedComment = portal.restrictedTraverse(portal.portal_url.getRelativeContentPath(comment))
    try:
        traversedComment.deleteDiscussion()
        countSuccess += 1
    except:
        countFail += 1

message = "deleted %s comments, failed to delete %s comments" % (countSuccess, countFail)
context.plone_utils.addPortalMessage(message)

pm = portal.portal_membership
member = pm.getMemberById(memberid)
if member is not None:
    pm.deleteMembers([memberid])
    message = "deleted member %s" % memberid
    context.plone_utils.addPortalMessage(message)

context.REQUEST['RESPONSE'].redirect( portal.absolute_url() )
