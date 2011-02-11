from zope import schema
from zope.interface import implements
from plone.app.users.userdataschema import IUserDataSchemaProvider
from plone.app.users.userdataschema import IUserDataSchema
from plone.app.users.browser.personalpreferences import UserDataPanelAdapter


class IPloneOrgUserDataSchema(IUserDataSchema):
    
    organization_title = schema.TextLine(title = u'Organization',
                                         required = False)
    organization_link = schema.TextLine(title = u'Organization home page',
                                        required = False)
    nickname = schema.TextLine(title = u'Nickname',
                               description = u'Your IRC nickname in the #plone channel',
                               required = False)


class PloneOrgUserDataSchemaProvider(object):
    implements(IUserDataSchemaProvider)

    def getSchema(self):
        return IPloneOrgUserDataSchema


class MemberProperty(object):
    
    def __init__(self, name):
        self.name = name
    
    def __get__(self, obj, type=None):
        return obj._getProperty(self.name)
    
    def __set__(self, obj, value):
        return obj.context.setMemberProperties({self.name: value})


class PloneOrgUserDataPanelAdapter(UserDataPanelAdapter):
    
    organization_title = MemberProperty('organization_title')
    organization_link = MemberProperty('organization_link')
    nickname = MemberProperty('nickname')
