import transaction
from AccessControl.SpecialUsers import system
from AccessControl.SecurityManagement import newSecurityManager
from Testing.makerequest import makerequest

app=makerequest(app)
newSecurityManager(None, system)

portal = app['plone.org']

utool = portal.portal_url
brains = portal.portal_catalog.searchResults(
    portal_type=("SiteUsingPlone", "Provider", "CaseStudy", "Buzz"))
count = 0

for brain in brains:
    count += 1
    obj = brain.getObject()
    obj._p_activate()
    if 'schema' in obj.__dict__:
        del obj.schema        

transaction.commit()
