
from django.core.mail import send_mail, BadHeaderError
from django.core.exceptions import ValidationError
from django.conf import settings
from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    name = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def send_mail(self):
        name = self.cleaned_data.get('name')
        from_email = self.cleaned_data.get('from_email')
        message = self.cleaned_data.get('message')
        subject = '<Contact Page Message from {}, email: {}>'\
            .format(name, from_email)
        try:
            to = settings.OUR_CONTACT_INFO.get('email')
            send_mail(subject, message, from_email, [to])
        except BadHeaderError:
            self.add_error(None, ValidationError(
                'Could not send email.\nExtra headers not allowed in'
                ' email body.',
                code='badheader'
            ))
            return False
        return True
