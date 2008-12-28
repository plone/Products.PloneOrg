from Products.CMFCore.utils import getToolByName
from StringIO import StringIO
import transaction

from AccessControl.SecurityManagement import newSecurityManager
from AccessControl.SecurityManager import setSecurityPolicy
from Testing.makerequest import makerequest
from Products.CMFCore.tests.base.security import PermissiveSecurityPolicy, OmnipotentUser
_policy=PermissiveSecurityPolicy()
_oldpolicy=setSecurityPolicy(_policy)
newSecurityManager(None, OmnipotentUser().__of__(app.acl_users))
app=makerequest(app)

attool = app['plone.org'].archetype_tool

def manage_updateSchema(self, REQUEST=None, update_all=None,
                        remove_instance_schemas=None):
    """Make sure all objects' schema are up to date.
    """
    out = StringIO()
    print >> out, 'Updating schema...'

    update_types = []
    if REQUEST is None:
        # DM (avoid persistency bug): avoid code duplication
        update_types = [ti[0] for ti in self.getChangedSchema() if ti[1]]
    else:
        # DM (avoid persistency bug):
        for t in self._listAllTypes():
            if REQUEST.form.get(t, False):
                update_types.append(t)
        update_all = REQUEST.form.get('update_all', False)
        remove_instance_schemas = REQUEST.form.get(
            'remove_instance_schemas', False)

    # XXX: Enter this block only when there are types to update!
    if update_types:
        # Use the catalog's ZopeFindAndApply method to walk through
        # all objects in the portal.  This works much better than
        # relying on the catalog to find objects, because an object
        # may be uncatalogable because of its schema, and then you
        # can't update it if you require that it be in the catalog.
        catalog = getToolByName(self, 'portal_catalog')
        portal = getToolByName(self, 'portal_url').getPortalObject()
        meta_types = [a['meta_type'] for a in self.listRegisteredTypes() if "%s.%s"%(a['package'],a['name']) in update_types]
        meta_types.remove("PSCFile")
        if remove_instance_schemas:
            func_update_changed = self._removeSchemaAndUpdateChangedObject
            func_update_all = self._removeSchemaAndUpdateObject
        else:
            func_update_changed = self._updateChangedObject
            func_update_all = self._updateObject
        if update_all:
            catalog.ZopeFindAndApply(portal, obj_metatypes=meta_types,
                search_sub=True, apply_func=func_update_all)
        else:
            catalog.ZopeFindAndApply(portal, obj_metatypes=meta_types,
                search_sub=True, apply_func=func_update_changed)
        for t in self.listRegisteredTypes():
            if t['meta_type'] in meta_types:
                print >> out, "Updating signature of %s" % (t['meta_type'])
                ident = "%s.%s"%(t['package'],t['name'])
                self._types[ident] = t['signature']
        self._p_changed = True

    print >> out, 'Done.'
    return out.getvalue()

transaction.commit()
print manage_updateSchema(attool, REQUEST=app.REQUEST)

