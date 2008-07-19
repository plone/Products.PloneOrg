from Products.CMFCore.utils import getToolByName
from Products.PluggableAuthService.interfaces.plugins import IUserEnumerationPlugin

def setupVarious(context):
    if context.readDataFile("deployment-various.txt") is None:
        return

    logger=context.getLogger("Products.PloneOrg")
    site=context.getSite()

    pas=getToolByName(site, "acl_users")
    pas.ZCacheable_setManagerId(manager_id="MemcachedManager")

    plugins=pas._getOb( 'plugins' )
    enumerators=plugins.listPluginIds(IUserEnumerationPlugin)
    # mutable_properties is very slow and we only need to search for
    # userids in source_users or in LDAP.
    for plugin in ('mutable_properties',):
        if plugin in enumerators:
            plugins.deactivatePlugin(IUserEnumerationPlugin, plugin)
