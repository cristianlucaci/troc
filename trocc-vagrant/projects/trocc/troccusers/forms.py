__author__ = 'marianlungu'
from django import forms
from .models import TroccUser
from . import log

class TroccUserForm(forms.ModelForm):
    class Meta:
        model = TroccUser
        fields = ('username', 'password')

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = TroccUser
        fields = ('username', 'password', 'email', 'first_name', 'last_name',)

    def save(self, commit=True):
        # Save the provided password in hashed format
        log.debug("Saving user")
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

