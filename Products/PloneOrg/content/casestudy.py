from Products.ATContentTypes.content import ATNewsItem
from Products.ATContentTypes.content.base import registerATCT
from Products.PloneOrg.config import PROJECTNAME


class CaseStudy(ATNewsItem):
    """A case study describes a succesfull Plone implementation."""

    meta_type        = "CaseStudy"
    portal_type      = "Case Study"
    archetype_name   = "Case Study"
    immediate_view   = "newsitem_view"
    default_view     = "newsitem_view"
    suppl_views      = ()
    _atct_newTypeDor = {}
    typeDescription  = "A case study describes a succesfull Plone implementation"
    assocMimetypes   = ()
    assocFileExt     = ()
    
registerATCT(CaseStudy, PROJECTNAME)
