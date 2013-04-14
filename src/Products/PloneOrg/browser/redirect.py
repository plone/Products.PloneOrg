class PloneOrgRedirectHandler(object):
    """ Handle some old resource location redirects to their newer equivalents.
    """

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self, url, host, port, path):
        """

        :param path: ZODB physical path to the current HTTP request context

        :return: None if no redirect needed, otherwise a string full HTTP URL to the redirect target

        :raise: zExceptions.Redirect or other custom redirect exception if needed
        """

        if not path:
            return

        # Developer manual front page
        if path in ["/plone.org/documentation/manual/developer-manual", "/plone.org/documentation/manual/developer-manual/"]:
            return "http://developer.plone.org"

        # Developer manual deep links
        if path.startswith("/plone.org/documentation/manual/developer-manual/"):
            return "http://developer.plone.org/moved_content.html"

        # Dexterity manual front page
        if path in ["/plone.org/products/dexterity/documentation", "/plone.org/products/dexterity/documentation/"]:
            return "http://developer.plone.org"

        # Dexterity manual deep links
        if path.startswith("/plone.org/products/dexterity/documentation"):
            return "http://developer.plone.org/moved_content.html"

        # No redirects
        return None
