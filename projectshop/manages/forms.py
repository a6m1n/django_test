"""Django forms file"""
from django import forms
from .models import Product, Order


class OrderForm(forms.Form):
    """From for create order"""
    product = forms.ModelChoiceField(
        queryset=Product.objects.filter(order=None),
    )
    client_phone_number = forms.CharField(max_length=30)
    status = forms.ChoiceField(choices=Order.STATUSES, required=True)
    date_create_order = forms.DateField(
        input_formats=["%d.%m.%Y"], required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        lists_fields = [
            'product', 'client_phone_number', 'status', 'date_create_order'
        ]

        for attr in lists_fields:
            self.fields[attr].widget.attrs.update({"class": "form-control"})

        self.fields['date_create_order'].widget.attrs.update(
            {"placeholder": "format: dd.mm.YYYY."}
        )

    def save(self):
        """ Save self object. Run this method from view """
        new_obj = Order.objects.create(
            product=self.cleaned_data["product"],
            client_phone_number=self.cleaned_data["client_phone_number"],
            status=self.cleaned_data["status"],
            date_create_order=self.cleaned_data["date_create_order"],
        )
        return new_obj


class ProductForm(forms.Form):
    """Form for create product"""

    name = forms.CharField(max_length=255, )
    start_price = forms.DecimalField(max_digits=5, decimal_places=2)
    create_date = forms.DateField(
        input_formats=["%d.%m.%Y"], help_text="Ex: 31.12.2000",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        lists_var = ['name', 'start_price', 'create_date']
        for attr in lists_var:
            self.fields[attr].widget.attrs.update({"class": "form-control"})

        self.fields['name'].widget.attrs.update(
            {"placeholder": "Product name"}
        )
        self.fields['create_date'].widget.attrs.update(
            {"placeholder": "format: dd.mm.YYYY."}
        )

        self.fields['start_price'].widget.attrs.update(
            {"placeholder": "Product price. Fromat: 10.99", }
        )

    def save(self):
        """ Save self object. Run this method from view """
        new_obj = Product.objects.create(
            name=self.cleaned_data["name"],
            start_price=self.cleaned_data["start_price"],
            create_date=self.cleaned_data["create_date"],
        )
        return new_obj
