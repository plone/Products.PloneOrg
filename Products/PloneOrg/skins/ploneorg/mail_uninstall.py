## Script (Python) "mail_uninstall"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=fromEmail=None,fromName=None,feedBack=None
##title=Mail script for uninstall information
##
# as of Nov 2005 Plone.org isnt running secure mail host (i think)

if fromEmail in [None, '']:
    fromEmail = "do-not-reply@plone.org"
else:
    # rudimentary hacking check
    assert fromEmail.count('@') == 1, "There must be one valid email address in the field"
    
if fromName in [None, '']:
    fromName = "Anonymous"
else:
    # rudimentary hacking check
    assert fromName.count('@') == 0, "Invalid name, it cannot contain a @"
    
to = "plone-feedback@lists.sourceforge.net"
url = context.absolute_url()

email = """From: %s <%s>
To: %s
Subject: Uninstallation feedback

%s

Generated from: %s""" % (fromName, fromEmail, to, feedBack, url)

context.MailHost.send(email)

redir = "/uninstall-feedback?portal_status_message=Feedback sent, thank you."

return context.REQUEST.RESPONSE.redirect(redir)
