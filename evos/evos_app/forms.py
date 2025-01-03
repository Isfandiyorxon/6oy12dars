from .models import Dish,Category,Coments
from django import forms

class OvqatFrom(forms.Form):
    name=forms.CharField(max_length=150,widget=forms.TextInput(attrs={
        "placeholder": "Ovqat nomi",
        'class': "form-control"
    }))

    about=forms.CharField(max_length=150,widget=forms.Textarea(attrs={
        "placeholder": "Ovqat haqida",
        'class': "form-control",
        'rows':3
    }))
    photo=forms.ImageField(required=False,widget=forms.FileInput())
    category=forms.ModelChoiceField(queryset=Category.objects.all(),
                               widget=forms.Select(attrs={
                                   'class': 'form-select'

                               }))
    def create(self):
        dish=Dish.objects.create(**self.cleaned_data)
        return dish

class RegistrationForm(forms.Form):
    username=forms.CharField(max_length=150,error_messages={"error":"max 150 ta belgi bo'lishi kerak"},
                             widget=forms.TextInput(attrs={
                                 'id':'form3Example1cg',
                                 "class": "form-control form-control-lg"
                             }))
    email=forms.EmailField(widget=forms.EmailInput(attrs={
        "id": "form3Example3cg",
        "class": "form-control form-control-lg"
    }))
    password=forms.CharField(min_length=4,widget=forms.PasswordInput(attrs={
        "id": "form3Example4cg",
        "class": "form-control form-control-lg"
    }))

    password_repeat=forms.CharField(min_length=4,widget=forms.PasswordInput(attrs={
        "id": "form3Example4cdg",
        "class": "form-control form-control-lg"
    }))

class LoginForm(forms.Form):
    username=forms.CharField(max_length=150,widget=forms.TextInput())
    password=forms.CharField(max_length=4,widget=forms.PasswordInput())


class ComentForm(forms.ModelForm):
    class Meta:
        model=Coments
        fields=['text']

class MyEmailForm(forms.Form):
    subject=forms.CharField(max_length=150,widget=forms.TextInput(attrs={
        "class":"form-control"
    }))
    message=forms.CharField(max_length=1000,widget=forms.Textarea(attrs={
        "class": "form-control",
        "maxlength":"1000",
        "rows":"4"

    }))