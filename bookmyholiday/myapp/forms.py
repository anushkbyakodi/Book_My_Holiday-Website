from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Customer, Place



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['place','type','description','location', 'url']

class CatalogForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields = ['customer','place','room_type','no_of_children','no_of_Adults','start_date','end_date','breakfast_included','cab_type','Total_price']
   