import transaction
import AccessControl
from Testing.makerequest import makerequest 

AccessControl.SecurityManagement.newSecurityManager(None, AccessControl.SpecialUsers.system)
app=makerequest(app) 
app['plone.org'].portal_catalog.manage_catalogRebuild()
transaction.commit()
