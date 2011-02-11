"""formlib integration of collective.recaptcha for use on the customized
registration form.
"""

from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from zope.app.form.browser.textwidgets import TextWidget

class RecaptchaWidget(TextWidget):
    """Widget that allows selecting from various offers, or entering an arbitrary code to obtain an offer."""
    __call__ = ViewPageTemplateFile('recaptcha_widget.pt')
