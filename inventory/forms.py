from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.models import User

class item_statusForm(forms.ModelForm):
    class Meta:
        model = item_status
        fields = ('item_code', 'item_name', 'type', 'price','status','item_quantity_available','issues',)


class SupplierForm(forms.ModelForm):
    class Meta:
        model = supplier
        fields = ('supplier_id', 'supplier_name', 'supplier_phone',)
        

class StaffForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class Sales_recordForm(forms.ModelForm):
    class Meta:
        model = sales_record
        fields = ('record_id', 'item_quantity_sold', 'item_code',)

class ReorderForm(forms.ModelForm):
    class Meta:
        model = reorder
        fields = ('order_id', 'date_reorder', 'quantity_reorder', 'date_of_receive','quantity_receive','item_code','supplier','remarks',)
