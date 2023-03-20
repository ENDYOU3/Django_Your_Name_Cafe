from django import forms
from app_product.models import *
from app_general.models import *

class ContactForm(forms.ModelForm):
	title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	description = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class':'form-control'}))
	class Meta:
		model = Contact
		fields = ('title','email','description')


class CustomerForm(forms.ModelForm):
	first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class':'form-control'}))
	country = forms.CharField(label="Country", widget=forms.TextInput(attrs={'class':'form-control'}))
	city = forms.CharField(label="City", widget=forms.TextInput(attrs={'class':'form-control'}))
	address = forms.CharField(label="Address", widget=forms.TextInput(attrs={'class':'form-control'}))
	phone = forms.CharField(label="Phone Number", widget=forms.TextInput(attrs={'class':'form-control'}))
	class Meta:
		model = Customer
		fields = ('first_name','last_name','country','city','address','phone')


class OrderDetailForm(forms.ModelForm):
	PAYMENT = [
        ('Cash On Delivery', 'Cash On Delivery'),
        ('Bank Transfer', 'Bank Transfer')
	]
	payment_method = forms.ChoiceField(label="Payment Method", required=True, choices=PAYMENT, widget=forms.RadioSelect)	
	note = forms.CharField(label="Message", initial="No Comment", widget=forms.TextInput(attrs={'class':'form-control'}))
	class Meta:
		model = Shipping
		fields = ('payment_method','note')