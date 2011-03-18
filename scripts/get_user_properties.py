"""When used as a script, this will print a comma separated list of
property values corresponding to the properties given on the command
line for each user named on stdin."""

from Products.CMFCore.utils import getToolByName

def getUserProperties(portal, usernames, properties):
    """Return a sequence of property values for each user specified"""
    for username in usernames:
        username = username.strip()
        acl_users = getToolByName(portal, 'acl_users')
        user = acl_users.getUser(username)
        yield tuple(user.getProperty(property, '') for property in properties)

if __name__ == '__main__':
    import sys
    from Testing.makerequest import makerequest

    app = makerequest(app)
    portal = app['plone.org']
    for properties in getUserProperties(portal, sys.stdin, sys.argv[1:]):
        print ', '.join(properties)
