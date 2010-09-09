"""Extend the user registration form to include a recaptcha.
"""

from zope.interface import Interface
from zope.formlib import form
from zope import schema
from zope.app.form.interfaces import WidgetInputError
from plone.app.users.browser.register import RegistrationForm
from Products.PloneOrg.browser.recaptcha_widget import RecaptchaWidget


class IRecaptcha(Interface):
    
    recaptcha = schema.TextLine(
        title = u'Enter the word below',
        description = u'This check is used to prevent spammers from using this form.',
        required = True,
        )


class PloneOrgRegistrationForm(RegistrationForm):
    
    @property
    def form_fields(self):
        form_fields = super(PloneOrgRegistrationForm, self).form_fields
        form_fields += form.Fields(IRecaptcha)
        form_fields['recaptcha'].custom_widget = RecaptchaWidget
        return form_fields

    def validate_registration(self, action, data):
        errors = super(PloneOrgRegistrationForm, self).validate_registration(action, data)
        
        captcha_view = self.context.restrictedTraverse('@@captcha')
        if not captcha_view.verify():
            err_str = u'You must correctly enter the word.'
            errors.append(WidgetInputError(
                    'recaptcha', u'Enter the word below', err_str))
            self.widgets['recaptcha'].error = err_str

        return errors
