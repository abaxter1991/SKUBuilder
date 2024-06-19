from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

from .models import ProductType, DesignPortfolio, Design, ProductPart, Color, Size, Product


class ProductModelForm(forms.ModelForm):
    color = forms.ModelChoiceField(queryset=ProductPart.objects.none())

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request')
        colors = ProductPart.objects.filter(product_part=request.colors)
        super(ProductModelForm, self).__init__(*args, **kwargs)
        self.fields['color'].queryset = colors


class ProductCreateModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'product_type',
            'design_portfolio',
            'design',
            'product_part',
            'color',
            'size',
        )


class DesignPortfolioModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        pass


class DesignVersionModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        pass


class ProductTypeModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        pass


class ProductPartModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        pass


class ColorModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        pass


class SizeModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        pass


