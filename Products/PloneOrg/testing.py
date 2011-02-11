from plone.app import testing


class PloneOrgFixture(testing.PloneSandboxLayer):
    default_bases = (testing.PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import Products.PloneOrg
        self.loadZCML(package=Products.PloneOrg)

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        self.applyProfile(portal, 'Products.PloneOrg:default')

PLONEORG_FIXTURE = PloneOrgFixture()
PLONEORG_FUNCTIONAL_TESTING = testing.FunctionalTesting(
    bases=(PLONEORG_FIXTURE,), name="PloneOrg:Functional")
