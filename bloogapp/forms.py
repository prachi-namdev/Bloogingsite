from django import forms
from bloogapp.models import blog,POSTBLOG
from django.contrib.auth.models import User

class signup(forms.ModelForm):
    class Meta:
        model=User
        fields= ('username','password','email','first_name','last_name')
        widgets = {'password':forms.PasswordInput()}

class postblog(forms.ModelForm):
    class Meta:
        model=POSTBLOG
        fields= ('title','description','image')
