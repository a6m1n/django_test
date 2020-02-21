""" Class test case django manages views """
from django.test import TestCase
from django.contrib.auth.models import User

from manages import models


class TestViews(TestCase):
    """Test django views"""
    fixtures = ['data_products.json', 'data_orders.json']

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='admin', password='123')
        user.is_superuser = True
        user.is_staff = True
        user.save()
        print("One.")

    def setUp(self):
        self.client.login(username="admin", password="123")

    def test_login(self):
        """ Django test login user """
        user_login = self.client.login(username="admin", password="123")
        self.assertTrue(user_login)
        response = self.client.get("/orders/")
        self.assertEqual(response.status_code, 200)

    def test_create_product_view_method_post_false_save(self):
        """ Test create product views. result - false """
        lengs = models.Product.objects.count()
        url = "/products/create"
        data = {
            'name': "test_prodcut",
            'start_price': 22,
            'create_date': "0101.2020",
        }
        self.client.post(url, data)
        self.assertEqual(lengs, models.Product.objects.count())

    def test_filter_in_orders_status(self):
        """ Testing my custom filter in order list page """
        response = self.client.get('/orders/')
        default_range = max(response.context['page_obj'].paginator.page_range)

        response = self.client.get('/orders/?status=New')
        pages_status_new = max(
            response.context['page_obj'].paginator.page_range)

        self.assertLess(pages_status_new, default_range)

    def test_filter_all_params(self):
        """ Check all params filter """
        response = self.client.get('/orders/')
        default_range = max(
            response.context['page_obj'].paginator.page_range)

        response = self.client.get(
            '/orders/?status=Payed&date_start=2002-12-01&date_end=2012-12-31')
        pages_status_new = max(
            response.context['page_obj'].paginator.page_range)

        self.assertLess(pages_status_new, default_range)

    def test_filter_no_validate_form_date_create_start(self):
        """Check filter no validate date create"""
        response = self.client.get('/orders/')
        default_range = max(
            response.context['page_obj'].paginator.page_range)

        response = self.client.get(
            '/orders/?date_start=31.12.2015')
        pages_status_new = max(
            response.context['page_obj'].paginator.page_range)
        self.assertEqual(pages_status_new, default_range)

    def test_filter_no_validate_form_date_create_stop(self):
        """Check filter no validate date stop"""
        response = self.client.get('/orders/')
        default_range = max(
            response.context['page_obj'].paginator.page_range)

        response = self.client.get(
            '/orders/?date_end=01.01/2000')
        pages_status_new = max(
            response.context['page_obj'].paginator.page_range)
        self.assertEqual(pages_status_new, default_range)

    def test_create_order_view_method_post_false_save(self):
        """ Testing create order view. Result false """
        lengs = models.Order.objects.count()
        url = "/orders/create"
        data = {
            'product': 2,
            'client_phone_number': '+248368742',
            'status': "N",
            'date_create_order': "0202.2020",
        }
        self.client.post(url, data)
        self.assertEqual(lengs, models.Order.objects.count())

    def test_order_update_view_true_save(self):
        """Test update view in orders. Save status = TRUE!"""
        obj = models.Order.objects.first()
        url = f"/orders/{obj.pk}/change"
        data = {
            'product': 2,
            'client_phone_number': obj.client_phone_number,
            'status': 'D',
            'date_create_order': obj.date_create_order,
        }
        r = self.client.post(url, data)
        new_url = '/orders/1'
        self.assertEqual(new_url, r.url)

    def test_generage_check_view_method_post(self):
        """Test generate check view. Or test redirect after POST requests"""
        obj = models.Order.objects.filter(status='P').first()
        url = f"/orders/{obj.pk}/check"

        r = self.client.post(path=url, pk=obj.pk)
        new_url = f'/orders/{obj.pk}/check/complete'
        self.assertEqual(new_url, r.url)

    def test_success_order_update_status(self):
        """testing success view and update object status after buy product"""
        obj = models.Order.objects.filter(status='D').first()
        url = f"/orders/{obj.pk}/check/complete"
        self.client.get(path=url)
        self.assertNotEqual(
            models.Order.objects.filter(pk=obj.pk).first().status,
            obj.status
        )

    def test_success_order_error(self):
        """ test update status iif it will be banned RESULT = FALSE"""
        obj = models.Order.objects.filter(status='P').first()
        url = f"/orders/{obj.pk}/check/complete"
        self.client.get(path=url)
        self.assertEqual(
            models.Order.objects.filter(pk=obj.pk).first().status,
            obj.status
        )
