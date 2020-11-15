from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, password_validation
from django.core import exceptions

class UserRegistrationForm(forms.ModelForm):
        
        
   
        password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
        password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
      


        class Meta:
            model = get_user_model()
            fields = [
                'username',
                'email']

        def clean(self):
            """
                validate attributes before saving to db
            """
            
            super(UserRegistrationForm, self).clean()
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            
            if (password1 != password2):
                raise forms.ValidationError(" The two passwords are not matching !!")
            
            try:
                password_validation.validate_password(password=password1, user=get_user_model())
            except exceptions.ValidationError as e:
                raise forms.ValidationError(list(e.messages))



        def save(self, commit=True):
            """
            Save user and passoword in hashed format
            """
            user=super(UserRegistrationForm, self).save(commit=False)
            user.set_password(self.cleaned_data.get("password1"))

            if commit:
                user.save()

            return user