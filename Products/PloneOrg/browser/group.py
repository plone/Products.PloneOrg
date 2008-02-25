from zope.interface import implements

from Products.CMFCore.utils import getToolByName
from Products.Five import BrowserView
from Products.PloneOrg.browser.interfaces import IGroupListing

#from Products.PloneLanguageTool import availablelanguages
#
#LANGUAGES = availablelanguages.languages

class GroupListing(BrowserView):
    implements(IGroupListing)

    def __init__(self, context, request):
        BrowserView.__init__(self, context, request)
        self.groupid = request.get('groupid', None)

        # Some private attributes which are here for performance reasons.
        props = getToolByName(context, 'portal_properties', None)
        if props is not None:
            stp = getattr(props, 'site_properties', None)
            if stp is not None:
                self._publicGroups = stp.getProperty('allowedPublicGroups', ())

        # If no id is given, use the first one in the allowed list
        if self.groupid is None and len(self._publicGroups) > 0:
            self.groupid = self._publicGroups[0]

        self._groupinfo = {}
        self._group = None
        self._gtool = getToolByName(context, 'portal_groups', None)
        if self._gtool is not None:
            self._groupinfo = self._gtool.getGroupInfo(self.groupid) or {}
            self._group = self._gtool.getGroupById(self.groupid) or None

    def title(self):
        title = self._groupinfo.get('title', None)
        return title and title or self.groupid

    def description(self):
        return self._groupinfo.get('description', None)

    def public(self):
        return self.groupid in self._publicGroups

    def groups(self):
        groups = []
        for groupid in self._publicGroups:
            info = self._gtool.getGroupInfo(groupid)
            info['id'] = groupid
            title = info['title']
            info['title'] = title and title or groupid
            info['selected'] = groupid == self.groupid or False
            groups.append(info)
        return groups

    def username(self, user):
        return user.getProperty('fullname') or \
               user.getUserName() or \
               user.getId()

    def users(self):
        if self._group is None:
            return []
        members = self._group.getGroupMembers()
        if not members:
            return []
        # A group can contain other groups, we are only interested in users
        members = (m for m in members if not self._gtool.isGroup(m))
        # Put all users without a description at the end
        users = []
        users2 = []
        for m in members:
            if not m.getProperty('description', None):
                users2.append(m)
            else:
                users.append(m)
        # Sort users by their name
        users.sort(key=self.username)
        users2.sort(key=self.username)
        return users + users2

    def language_name(self, langcode):

        #XXX: Not sure if this will work ...
        portal_languages = getToolByName(self.context, 'portal_languages')
        LANGUAGES = portal_languages.getAvailableLanguages()

        language = LANGUAGES.get(langcode, None)
        if language is None:
            return langcode
        return language.get('english', langcode)
