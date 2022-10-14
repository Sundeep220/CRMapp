from django.forms import ModelForm
from .models import *


#since we are creating an order form
class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'