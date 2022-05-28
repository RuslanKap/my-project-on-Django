from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Имя")
    age = forms.CharField(label="Возраст")
