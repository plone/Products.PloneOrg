try:
    from Products.LinguaPlone.public import *
except ImportError:
    # No multilingual support
    from Products.Archetypes.public import *
from Products.ATContentTypes.content.folder import ATFolder
from Products.ATContentTypes.content.base import registerATCT
from Products.CMFPlone.utils import _createObjectByType
from Products.PloneOrg.config import PROJECTNAME

IndustrySchema = Schema((
    StringField("mailinglistInfo",
        searchable = False,
        required   = False,
        widget     = StringWidget(
            i18n_domain  = "ploneorg",
            label        = "URLfor mailinglist information",
            label_msgid  = "label_mailinglistinfo",
            ),
    ),
    StringField("mailinglistarchive",
        searchable = False,
        required   = False,
        widget     = StringWidget(
            i18n_domain  = "ploneorg",
            label        = "URLfor mailinglist archive",
            label_msgid  = "label_mailinglistarchive",
            ),
    ),
    ))

class Industry(ATFolder):
    """Industry information package."""
    meta_type        = "Industry"
    portal_type      = "Industry information"
    archetype_name   = "Industry informationFolder"
    immediate_view   = "ploneorg_industry"
    default_view     = "ploneorg_industry"
    suppl_views      = ()
    _atct_newTypeDor = {}
    typeDescription  = "Industry information package"
    assocMimetypes   = ()
    assocFileExt     = ()
    
    schema           = ATFolderSchema.copy() + IndustrySchema

    def at_post_create_script(self):
        self.at_post_edit_script()

        _createObjectByType("Folder", self, id="case-studies",
                title="Case studies")




registerATCT(CaseStudy, PROJECTNAME)
            

