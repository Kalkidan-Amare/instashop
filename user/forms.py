from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'store_name', 'phone_number')

    def clean_store_name(self):
        store_name = self.cleaned_data.get('store_name')
        if not store_name:
            store_name = self.cleaned_data.get('username')
        return store_name

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'store_name', 'phone_number']