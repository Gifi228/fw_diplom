from django import forms
from .models import *

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'description',
            'photo',
            'category'
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Article Title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Article Content'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            })
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Username",
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Username ...'
                               }))

    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Password ...'
                               }))


class RegistrationUserForm(UserCreationForm):
    username = forms.CharField(label="Username",
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Username ...'
                               }))

    first_name = forms.CharField(label="Your First Name",
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control',
                                     'placeholder': 'First name ...'
                                 }))

    last_name = forms.CharField(label="Your Last Name",
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Last name ...'
                                }))

    email = forms.EmailField(label="Your Email",
                             widget=forms.TextInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'Your email ...'
                             }))
    password1 = forms.CharField(label="Create Password",
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Password ...'
                                }))
    password2 = forms.CharField(label="Confirm Password",
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Password ...'
                                }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',
                  'password1', 'password2')


class UserForm(forms.ModelForm):
    username = forms.CharField(label="Username",
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Username ...'
                               }))

    first_name = forms.CharField(label="Your First Name",
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control',
                                     'placeholder': 'First name ...'
                                 }))

    last_name = forms.CharField(label="Your Last Name",
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Last name ...'
                                }))

    email = forms.EmailField(label="Your Email",
                             widget=forms.TextInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'Your email ...'
                             }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', 'mobile', 'address', 'job', 'image')

        widgets = {
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number'
            }),
            'mobile': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Mobile Number'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Address'
            }),
            'job': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Job'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

        widgets = {
            'text': forms.Textarea(attrs={
                "class": 'form-control',
                "placeholder": "Writing your comment",
                "rows": 5
            })
        }





