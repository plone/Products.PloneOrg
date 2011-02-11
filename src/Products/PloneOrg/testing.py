from plone.app import testing

from Products.CMFCore.utils import getToolByName


class PloneOrgFixture(testing.PloneSandboxLayer):
    default_bases = (testing.PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import Products.PloneOrg
        self.loadZCML(package=Products.PloneOrg)

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        self.applyProfile(portal, 'Products.PloneOrg:default')

        # Add some members to some groups for testing the team page
        portal_membership = getToolByName(portal, 'portal_membership')
        gtool = getToolByName(portal, 'portal_groups')

        portal_membership.addMember(
            'limi', 'secret', ['Member'], ())
        gtool.addPrincipalToGroup('limi', 'Founders')

        portal_membership.addMember(
            'runyaga', 'secret', ['Member'], ())
        gtool.addPrincipalToGroup('runyaga', 'Founders')

        portal_membership.addMember(
            'esteele', 'secret', ['Member'], ())
        gtool.addPrincipalToGroup('esteele', 'ReleaseManagers')

PLONEORG_FIXTURE = PloneOrgFixture()
PLONEORG_FUNCTIONAL_TESTING = testing.FunctionalTesting(
    bases=(PLONEORG_FIXTURE,), name="PloneOrg:Functional")
