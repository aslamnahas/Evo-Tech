from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customer  # Import the Customer model from models.py within the same directory

# Create your forms here.
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=20)

    class Meta:
        model = Customer
        fields = ("email", "username", "password1", "password2")  # Include "username" instead of "referral" if not present in Customer model

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)