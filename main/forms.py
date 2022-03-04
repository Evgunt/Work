from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from datetime import datetime

from .models import AdvUser, keys


class RegisterUserForm(forms.ModelForm):
    key = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField()

    def clean_password1(self):
        password = self.cleaned_data['password']
        if password:
            password_validation.validate_password(password)
        return password

    def clean(self):
        super().clean()
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        num = self.cleaned_data['key']
        errors = {}
        if keys.objects.filter(number=num, owner='Отсутствует').exists():
            pass
        else:
            errors['key'] = ValidationError(
                'Несуществующий ключ', code='key_errors'
            )
        if password and password2 and password != password2:
            errors['password2'] = ValidationError(
                'Введенные пароли не совпадают', code='password_mismatch'
            )
        if errors != '':
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.date = datetime.now()
        user.email = user.username
        key = keys.objects.get(number=user.key, owner='Отсутствует')
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            key.owner = user
            key.save()
        return user

    class Meta:
        model = AdvUser
        fields = ('username', 'password', 'password2', 'first_name', 'key')


class loginForm(forms.Form):
    key = forms.CharField(required=False)
    username = forms.EmailField(required=False)
    password = forms.PasswordInput()

    class Meta:
        fields = ('username', 'password', 'key')


class help_form(forms.Form):
    title = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    content = forms.CharField(required=True)
    files = forms.FileField()

    class Meta:
        fields = ('title', 'email', 'content', 'files')
