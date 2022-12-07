from django import forms
from django.forms import ModelForm 
from .models import Vehiculo,Reserva_Inicial1
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class VehiculoForm(ModelForm):

    class Meta:
        model = Vehiculo
        fields = '__all__'
        
class Reserva_Inicial1Form(ModelForm):

    class Meta:
        model = Reserva_Inicial1
        fields = '__all__'

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email', 'password', 'is_active','is_staff','is_superuser']
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control input_for_form','placeholder':'Enter Username','autofocus':True}),
            'first_name':forms.TextInput(attrs={'class':'form-control input_for_form','placeholder':'Enter Firstname'}),
            'last_name':forms.TextInput(attrs={'class':'form-control input_for_form','placeholder':'Enter Lastname'}),
            'email':forms.EmailInput(attrs={'class':'form-control input_for_form','placeholder':'Enter E-Mail'}),
            'password':forms.TextInput(attrs={'class':'form-control input_for_form','placeholder':'Enter Password'}),
            'is_active':forms.CheckboxInput(attrs={'class':'mx-auto','id':'toggle'}),
            'is_staff':forms.CheckboxInput(attrs={'class':'mx-auto','id':'is_staff_user'}),
            'is_superuser':forms.CheckboxInput(attrs={'class':'mx-auto','id':'is_super_user'}),
        }
        labels = { # === this is for customize field label ===
            'username':'Username',
            'first_name':'Firstname',
            'last_name':'Lastname',
            'email':'E-Mail',
            'password':'Password',
            'is_active':'Active',
            'is_staff':'Staff',
            'is_superuser':'Super',
        }
