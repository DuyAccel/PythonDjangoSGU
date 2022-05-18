
from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class MyUserCreationForm(UserCreationForm):
    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
    }

    username = forms.CharField(required=True, label='Username', widget=forms.TextInput(
            attrs={'placeholder':'Enter your username...',
                    'id':'inputUsername'
            }
    ))

    email = forms.EmailField(required=True,label='Email', widget=forms.EmailInput(
            attrs={'placeholder':'Enter your email...',
                    'id':'inputEmail'}
    ))

    password1 = forms.CharField(required=True,label=("Password"),
        widget=forms.PasswordInput(
            attrs={'placeholder':"Enter your password...",
                    'id' : 'inputPassword'
                }))

    password2 = forms.CharField(required=True,label=("Password Confirmation"),
        widget=forms.PasswordInput(
            attrs={'placeholder':"Enter confirm password...",
                    'id':'inputCFPassword'
                }),
        help_text=("Enter the same password as above, for verification."))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(MyUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.set_email = self.cleaned_data['email']
        if commit:
            user.save()
        return user