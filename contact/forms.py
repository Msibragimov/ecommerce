from django import forms
from contact.models import Contact
from contact.validators import validate_number, validate_name_or_surname


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','surname', 'email', 'phone_number', 'message']
    

    def clean(self):
        cleaned_data = super().clean()
        phone_number = cleaned_data.get('phone_number')
        name = cleaned_data.get('name')
        surname = cleaned_data.get('surname')
        validate_number(phone_number)
        validate_name_or_surname(name)
        validate_name_or_surname(surname)
        return cleaned_data    
    
    