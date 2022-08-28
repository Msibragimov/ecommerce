from django import forms
from contact.models import Contact
from contact.validators import validate_number, validate_name_or_surname


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','surname', 'email', 'phone_number', 'message']
    
    def validate_phone_number(self, value):
        validate_number(value)

    def validate_name(self, value):
        validate_name_or_surname(value)
    
    def validate_surname(self, value):
        validate_name_or_surname(value)
    
    
    