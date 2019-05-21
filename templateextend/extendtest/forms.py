from django import forms
from .models import User


# class AddFom(forms.Form):
#     a = forms.IntegerField()
#     b = forms.IntegerField()

class AddFom(forms.ModelForm):
    class Meta():
        model = User
        fields = ['username', 'password']