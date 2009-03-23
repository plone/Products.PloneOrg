from zope.interface import implements
from Products.CacheSetup.interfaces import IPurgeUrls

class FrontpagePurger(object):
    implements(IPurgeUrls)

    def __init__(self, context):
        self.context=context

    def getRelativeUrls(self):
        return [''] # the front page

    def getAbsoluteUrls(self, relativeUrls):
        return []
