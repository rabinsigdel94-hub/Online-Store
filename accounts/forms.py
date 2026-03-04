from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Address, Profile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['full_name', 'phone', 'address_line1', 'address_line2', 
                  'city', 'state', 'postal_code', 'country', 'is_default']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'date_of_birth']
