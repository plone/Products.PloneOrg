class PloneOrgRedirectHandler(object):
    """ Handle some old resource location redirects to their newer equivalents.
    """

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self, url, host, port, path):
        """

        :param path: Path as written in HTTP request (not site virtual path)

        :return: None if no redirect needed, otherwise a string full HTTP URL to the redirect target

        :raise: zExceptions.Redirect or other custom redirect exception if needed
        """

        if not path:
            return

        # Translate to virtual path, so that this works in local dev and prod
        if path.startswith("/plone.org"):
            path = path.replace("/plone.org", "")

        # Developer manual front page
        if path in ["/documentation/manual/developer-manual", "/documentation/manual/developer-manual/"]:
            return "http://developer.plone.org"

        # Developer manual deep links
        if path.startswith("/documentation/manual/developer-manual/"):
            return "http://developer.plone.org/moved_content.html"

        # Theme reference
        if path in ["/documentation/manual/theme-reference", "/documentation/manual/theme-reference/"]:
            return "http://developer.plone.org/#theme-development"

        # Theme reference deep links
        if path.startswith("/documentation/manual/theme-reference/"):
            return "http://developer.plone.org/moved_content.html"

        # Dexterity manual front page
        if path in ["/products/dexterity/documentation", "/products/dexterity/documentation/"]:
            return "http://developer.plone.org"

        # Dexterity manual deep links
        if path.startswith("/products/dexterity/documentation"):
            return "http://developer.plone.org/moved_content.html"

        # No redirects
        return None
