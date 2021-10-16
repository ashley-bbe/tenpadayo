from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import cloudinary
from django.http import request
from .models import Product, Wishlist

# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = '__all__'


PRODUCT_TYPE = [
	('shampoo','Shampoo'), ('conditioner', 'Conditioner'), 
	('deep conditioner', 'Deep Conditioner'),
	('leave-in conditioner', 'Leave-in Conditioner'), ('gel', 'Gel'), 
	('mousse', 'Mousse'), ('oil','Oil'), ('serum', 'Serum')
]

PRODUCT_BRAND = [
	('shea moisture', 'Shea Moisture'), ('curlsmith', 'Curlsmith'),
	('cantu', 'Cantu'), ('boucleme', 'Bouclème'),
	("not your mother's", "Not Your Mother's"), ('avril', 'Avril'),
	('tropikalbliss', 'Tropikalbliss')
]

HAIR_TYPE = [
	('2a', '2A'), ('2b', '2B'), ('2c', '2C'), 
	('3a', '3A'), ('3b', '3B'), ('3c', '3C'), 
	('4a', '4A'), ('4b', '4B'), ('4c', '4C') 
]

HAIR_TEXTURE = [
	('fine hair', 'Fine Hair' ),
	('medium hair', 'Medium Hair'),
	('coarse hair', 'Coarse Hair')
]

HAIR_POROSITY = [
	('low porosity', 'Low Porosity' ),
	('medium porosity', 'Medium Porosity'),
	('high porosity', 'High Porosity')
]


class ProdType(forms.Form):
	product_type = forms.CharField(label='search_product', 
	widget=forms.Select(choices=PRODUCT_TYPE))

class ProdBrand(forms.Form):
	product_type = forms.CharField(label='search_brand',
	widget=forms.Select(choices=PRODUCT_BRAND))	

class HairType(forms.Form):
	hair_type = forms.CharField(label='hair_type',
	widget=forms.Select(choices=HAIR_TYPE))	

class HairTexture(forms.Form):
	hair_texture = forms.CharField(label='hair_texture',
	widget=forms.Select(choices=HAIR_TEXTURE))	

class HairPorosity(forms.Form):
	hair_porosity = forms.CharField(label='hair_porosity',
	widget=forms.Select(choices=HAIR_POROSITY))	