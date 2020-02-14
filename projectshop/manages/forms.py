from django import forms
from .models import Product, Sale, Order


class OrderForm(forms.Form):
    product = forms.ModelChoiceField(queryset= Product.objects.filter(order=None),)
    client_phone_number = forms.CharField(max_length=30)
    status = forms.ChoiceField(choices=Order.STATUSES, required=True)
    date_create_order = forms.DateField(input_formats=['%d.%m.%Y'], required=False,)

    product.widget.attrs.update({"class":"form-control"})
    client_phone_number.widget.attrs.update({"class":"form-control"})
    status.widget.attrs.update({"class":"form-control"})
    date_create_order.widget.attrs.update({"placeholder": "format: dd.mm.YYYY.", "class": "form-control"})

    def save(self):
        new_obj = Order.objects.create(
            product=self.cleaned_data['product'],
            client_phone_number=self.cleaned_data['client_phone_number'],
            status=self.cleaned_data['status'],
            date_create_order=self.cleaned_data['date_create_order'],
        )
        return new_obj


class ProductForm(forms.Form):
    name = forms.CharField(max_length=255)
    start_price = forms.DecimalField(max_digits=5, decimal_places=2)
    sale = forms.ModelChoiceField(queryset=Sale.objects.all(), label='Sale!: ', required=False, )
    create_date = forms.DateField(input_formats=['%d.%m.%Y'], help_text='Ex: 31.12.2000')

    name.widget.attrs.update({"placeholder": "Product name", "class": "form-control"})
    start_price.widget.attrs.update({"placeholder": "Product price. Fromat: 10.99", "class": "form-control"})
    sale.widget.attrs.update({"placeholder": "Sale!", "class": "form-control"})
    create_date.widget.attrs.update({"placeholder": "format: dd.mm.YYYY.", "class": "form-control"})

    def save(self):
        new_obj = Product.objects.create(
            name=self.cleaned_data['name'],
            start_price=self.cleaned_data['start_price'],
            create_date=self.cleaned_data['create_date'],
        )
        if self.cleaned_data['sale']:
            new_obj.sale.add(self.cleaned_data['sale'])

        return new_obj
