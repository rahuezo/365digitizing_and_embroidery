from django import forms
from crispy_forms.helper import FormHelper
from django.contrib.auth import (authenticate, get_user_model, login, logout)

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                                       'class': 'input-lg'}))
    password = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Password',
                                                                       'class': 'input-lg', 'type': 'password'}))

    helper = FormHelper()

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if not user:
            raise forms.ValidationError("This user does not exist!")

        if not user.check_password(password):
            raise forms.ValidationError("Incorrect password!")

        if not user.is_active:
            raise forms.ValidationError("This user is no longer active!")

        return super(UserLoginForm, self).clean()


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                                         'class': 'input-lg'}))

    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                                       'class': 'input-lg'}))
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                                       'class': 'input-lg'}))
    email1 = forms.EmailField(label="", widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                                       'class': 'input-lg'}))
    email2 = forms.EmailField(label="", widget=forms.TextInput(attrs={'placeholder': 'Confirm Email',
                                                                       'class': 'input-lg'}))

    password1 = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Password',
                                                                       'class': 'input-lg', 'type': 'password'}))

    password2 = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Confirm Password',
                                                                       'class': 'input-lg', 'type': 'password'}))

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email1',
            'email2',
            'password1',
            'password2',
        ]

    def clean_email2(self):
        email1 = self.cleaned_data.get('email1')
        email2 = self.cleaned_data.get('email2')

        if email1 != email2:
            raise forms.ValidationError("Emails must match!")

        # Check if email already exists

        email_qs = User.objects.filter(email=email1)

        if email_qs.exists():
            raise forms.ValidationError("This email has already been registered!")

        return email1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError("Passwords must match!")

        return password1






















