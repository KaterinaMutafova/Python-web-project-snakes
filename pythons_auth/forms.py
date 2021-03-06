from bootstrap4.templatetags import bootstrap4
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from pythons_auth.models import UserProfile


# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password', 'email')
#         widgets = {
#             'password': forms.PasswordInput(),
#             'email': forms.EmailInput(),
#         }

#     def clean_email(self):
#         email = self.cleaned_data.get('email', False)
#         if not email:
#             raise forms.ValidationError("Email is required!")
#         return email



class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {
            'password': forms.PasswordInput(),
            'email': forms.EmailInput(),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email', False)
        if not email:
            raise forms.ValidationError("Email is required!")
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(),
    )