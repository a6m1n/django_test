from django.test import TestCase

from manages import forms
from manages import models


class TestViews(TestCase):
    """Test django views"""
    fixtures = ['data_products.json', 'data_orders.json']

    def test_create_product_from(self):
        all_products = models.Product.objects.count()
        data = {
            'name': "test_prodcut",
            'start_price': 22,
            'create_date': "2020-10-10",
        }
        form = forms.ProductForm(data=data)
        self.assertTrue(form.is_valid())
        form.save()

        self.assertNotEqual(all_products, models.Product.objects.count())

    def test_ProductForm_clean_false_save(self):
        data = {
            'name': "test_prodcut",
            'start_price': -22,
            'create_date': "2020-10-10",
        }
        form = forms.ProductForm(data=data)
        resp = form.errors.as_data().get('start_price')[0]
        self.assertEqual(resp.message, 'Enter a price > 1')
