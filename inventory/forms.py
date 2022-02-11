from django import forms
from .models import *

class InventoryForm(forms.ModelForm):

    class Meta:
        model = Inventory
        fields = '__all__'
