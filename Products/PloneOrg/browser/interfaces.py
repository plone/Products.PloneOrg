from zope.interface import Interface, Attribute

class IGroupListing(Interface):
    """Interface for a listing of all members of a group."""

    id = Attribute("The id of the viewed group.")

    def title():
        """A human readable title of the group."""

    def description():
        """A short description of the group."""

    def public():
        """Is the group publicly viewable."""

    def groups():
        """Returns a list of all publicly viewable groups."""

    def users():
        """Returns a list of all users who are members of the group."""

    def username(username):
        """Returns the user name of a user."""

    def language_name(langcode):
        """Returns the full language name for a language code."""
