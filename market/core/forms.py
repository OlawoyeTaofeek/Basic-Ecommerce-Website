from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import ContactProfile
 



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
         'placeholder': 'Enter Your Username',
         'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
         'placeholder': 'Enter Password',
         'class': 'w-full py-4 px-6 rounded-xl'
    }))

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(widget=forms.TextInput(attrs={
         'placeholder': 'Enter Your Username',
         'class': 'w-full py-4 px-6 rounded-xl'
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
         'placeholder': 'Enter Your Valid Email',
         'class': 'w-full py-4 px-6 rounded-xl'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
         'placeholder': 'Enter Password',
         'class': 'w-full py-4 px-6 rounded-xl'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
         'placeholder': 'Confirm Password',
         'class': 'w-full py-4 px-6 rounded-xl'
    }))



class ContactForm(forms.ModelForm):
     class Meta:
          model = ContactProfile
          fields = '__all__'
          exclude = ('timestamp',)
     
     name = forms.CharField(max_length=254, required=True, 
          widget=forms.TextInput(attrs={
               'placeholder': 'Enter Your Name',
               'class': 'w-full py-4 px-6 rounded-xl'
     }))
     
     email = forms.EmailField(max_length=254, required=True, 
          widget=forms.TextInput(attrs={
               'placeholder': 'Enter Your Email',
               'class': 'w-full py-4 px-6 rounded-xl'    
     }))
     
     message = forms.CharField(max_length=2000, required=True, 
		widget=forms.Textarea(attrs={
			'placeholder': 'Message..',
			'class': 'w-full py-4 px-6 rounded-xl',
	}))
     
