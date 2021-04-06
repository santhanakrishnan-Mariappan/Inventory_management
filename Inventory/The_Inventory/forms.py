from django import forms
from .models import *


class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = '__all__'

class DesktopForm(forms.ModelForm):
    class Meta:
        model = DeskTop
        fields = '__all__'

class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = '__all__'


