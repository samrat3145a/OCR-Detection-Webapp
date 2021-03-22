from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

from MainApp.models import ImageSave, PdfSave , DocxSave

class ImageUpload(forms.ModelForm):
    class Meta:
        model = ImageSave
        fields = '__all__'


class PdfUpload(forms.ModelForm):
    class Meta:
        model = PdfSave
        fields = '__all__'
        

class DocxUpload(forms.ModelForm):
    class Meta:
        model = DocxSave
        fields = '__all__'


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **krwargs):
        super(SignupForm, self).__init__(*args, **krwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = ' '

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = ''

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = ' '