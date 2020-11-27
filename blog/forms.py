
from django.forms import ModelForm
from .models import Post, Category
from django import forms
from users.models import Signup

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        #field = ('title', 'overview', 'image')

class EmailSignupForm(forms.ModelForm):

    class Meta:
        model = Signup
        fields = ['email', ]
        def clean_email(self):
            email = self.cleaned_data.get('email')
            return email