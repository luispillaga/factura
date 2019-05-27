from django import forms
from django.contrib.auth.models import User
from company.models import Company


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Contraseña", required=True, widget=forms.PasswordInput(
        attrs={'class':'input100'}
    ))
    password2 = forms.CharField(label="Contraseña", required=True, widget=forms.PasswordInput(
        attrs={'class':'input100'}
    ))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control form-control-alternative'}),
            'last_name': forms.TextInput(attrs={'class':'form-control form-control-alternative'}),
            'email': forms.EmailInput(attrs={'class':'form-control form-control-alternative'}),
        }


class CompanyEditForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'address', 'phone', 'city', 'logo')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control form-control-alternative'}),
            'address': forms.TextInput(attrs={'class':'form-control form-control-alternative'}),
            'phone': forms.TextInput(attrs={'class':'form-control form-control-alternative'}),
            'city': forms.TextInput(attrs={'class':'form-control form-control-alternative'}),
            'logo': forms.FileInput(attrs={'class':'form-control form-control-alternative'}),
        }
