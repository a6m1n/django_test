from django.test import TestCase

from manages import forms
from manages import models


class TestViews(TestCase):
    """Test django views"""
    fixtures = ['data_products.json', 'data_orders.json']

    @classmethod
    def setUpTestData(cls):
        print("One.")

    def test_create_product_from(self):
        all_products = models.Product.objects.count()
        data={
            'name': "test_prodcut",
            'start_price': 22,
            'create_date': "01.01.2020",
        }
        form = forms.ProductForm(data=data)
        self.assertTrue(form.is_valid())
        form.save()

        self.assertNotEqual(all_products, models.Product.objects.count())

    def test_create_order_from(self):
        all_orders = models.Order.objects.count()
        data={
            'product': 2,
            'client_phone_number': '+248368742',
            'status': "N",
            'date_create_order':"02.02.2020",
        }
        form = forms.OrderForm(data=data)

        self.assertTrue(form.is_valid())
        form.save()
        self.assertNotEqual(all_orders, models.Order.objects.count())
