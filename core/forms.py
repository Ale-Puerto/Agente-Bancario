from django import forms
from .models import *

class CuentaForm(forms.ModelForm):
    
    class Meta:
        model = Cuenta
        fields = ("IdCuenta","PIN")
