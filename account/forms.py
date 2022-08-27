from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


# Create your forms here.

class RegistrationForm(UserCreationForm, forms.ModelForm):

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs) -> None:
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control','placeholder':'Enter Username'})
        self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':'Enter email'})
        self.fields['password1'].widget.attrs.update({'class':'form-control','placeholder':'Enter password'})
        self.fields['password2'].widget.attrs.update({'class':'form-control','placeholder':'Enter password confirmation'})

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class UserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"autofocus": True}))

    class Meta:
        model = User
        fields = ('username', 'password')
        
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args,**kwargs)
        
        self.fields['username'].widget.attrs.update({'class':'form-control','placeholder':'Email or Username'})
        self.fields['password'].widget.attrs.update({'class':'form-control','placeholder':'Password'})