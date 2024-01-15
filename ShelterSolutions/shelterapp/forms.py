from django import forms
from django.contrib.auth.models import User

class userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    conf = forms.CharField(max_length=20,widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','conf']

class userlogin(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)