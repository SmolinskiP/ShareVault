from django import forms
from .models import File
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from .widgets import AdminFileWidget

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['filename', 'file']

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label=_("Nazwa użytkownika"),
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label=_("Hasło"),
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

class AdminFileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = '__all__'
        widgets = {
            'file': AdminFileWidget,
        }
