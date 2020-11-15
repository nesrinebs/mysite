from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django import forms


class UserEditForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput)
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput)
    email = forms.CharField(label='Email', widget=forms.EmailInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def save(self, commit=True):
        user = super(UserEditForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
