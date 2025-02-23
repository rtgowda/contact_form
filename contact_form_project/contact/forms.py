from django import forms
from .models import ContactMessage
import re

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit() or len(phone) != 10:
            raise forms.ValidationError("Phone number must contain exactly 10 digits.")
        return phone

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@company.com'):
            raise forms.ValidationError("Only company emails (@company.com) are allowed.")
        return email
