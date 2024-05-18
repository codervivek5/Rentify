from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Property

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['place', 'area', 'bedrooms', 'bathrooms', 'nearby_hospitals', 'nearby_colleges']

    def clean(self):
        cleaned_data = super().clean()
        area = cleaned_data.get('area')
        if area <= 0:
            self.add_error('area', 'Area must be a positive number')
