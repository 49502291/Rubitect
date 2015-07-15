from django.forms import ModelForm
from django import forms
from .models import Doctor
from .models import FamilyMember
from .models import Patient


class DoctorForm(ModelForm):
	class Meta:
		model = Doctor
		exclude = ['id']


class PatientForm(ModelForm):
	class Meta:
		model = Patient
		exclude = ['id', 'doctor']

class FamilyForm(ModelForm):
	class Meta:
		model = FamilyMember
		exclude = ['id','patients']


class LoginForm(forms.Form):
	TYPE =(('Patient','Patient'),('Doctor', 'Doctor'),('FamilyMember', 'FamilyMember'))
	username = forms.CharField(required = True, error_messages = {'required': 'Please input username'})
	password = forms.CharField(required = True, error_messages = {'required': 'Please input password'},
		 					   widget = forms.PasswordInput(attrs= {'placeholder' : 'password',}))
	accounttype = forms.ChoiceField(required =True, choices = TYPE)
