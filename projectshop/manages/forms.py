"""Django forms file"""
import datetime

from django import forms
from django.forms import ModelForm

from typing import Any, Dict

from .models import Product, Order


class FormControlMixin:
    """From control mixin who add class form-control to all fields"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})


class OrderForm(FormControlMixin, ModelForm):
    """Class order form. Validation phone and date this!"""
    product = forms.ModelChoiceField(
        queryset=Product.objects.filter(order=None), )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['date_create_order'].widget.attrs.update(
            {"placeholder": "format: YYYY-mm-dd ."}
        )
        self.fields['client_phone_number'].widget.attrs.update(
            {"placeholder": "format: 0505455444"}
        )

    def clean(self) -> Any:
        super().clean()
        phone_data = self.cleaned_data.get('client_phone_number')

        if len(phone_data) != 10 or not phone_data.isnumeric():
            self._errors['client_phone_number'] = self.error_class([
                'Invalid phone number'])

        date_str = self.cleaned_data.get('date_create_order')
        if not isinstance(date_str, datetime.date):
            self._errors['date_create_order'] = self.error_class([
                'Invalid date format'])

        return self.cleaned_data

    class Meta:
        model = Order
        fields = [
            'product', 'client_phone_number',
            'status', 'date_create_order'
        ]


class ProductForm(FormControlMixin, ModelForm):
    """Form for create product"""
    def __init__(self, *args, **kwargs):
        """added html attrs to class (added only to form!)"""
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update(
            {"placeholder": "Product name"})

        self.fields['create_date'].widget.attrs.update(
            {"placeholder": "format: YYYY.mm.dd."})

        self.fields['start_price'].widget.attrs.update(
            {"placeholder": "Product price. Fromat: 10.99", })

    def clean(self) -> Any:
        super().clean()
        print(self.cleaned_data.get('start_price'))
        if int(self.cleaned_data.get('start_price')) < 1:
            self._errors['start_price'] = self.error_class([
                'Enter a price > 1'
            ])

        return self.cleaned_data

    class Meta:
        model = Product
        fields = [
            'name', 'start_price',
            'create_date'
        ]


class FilterViewForm(FormControlMixin, forms.Form):
    """Class filter form in list order (filter orders)"""
    date_start = forms.DateField(initial=datetime.date.today, required=False)
    date_end = forms.DateField(initial=datetime.date.today, required=False)

    def clean(self) -> Dict[Any, Any]:
        super().clean()
        status = self.data.get("status")

        if status:
            self.cleaned_data["status"] = status
        return self.cleaned_data
