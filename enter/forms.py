from django import forms
from enter.models import User, Product, Store


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('Name', 'Category', 'is_favorite')


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ('Title', 'Owner', 'is_favorite')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('Names', 'Email')
