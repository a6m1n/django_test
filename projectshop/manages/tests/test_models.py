from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType


from manages import models
from sales.models import AllTimeDiscount, Sale


class TestViews(TestCase):
    """Test django models"""
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

    def create_object_sale(self):
        """Create objects sales"""
        product = models.Product.objects.all().first()
        all_disct = AllTimeDiscount.objects.create(
            name='test',
            discount='50',
        )
        Sale.objects.create(
            name="Classic all-time sale",
            product=product,
            content_type=ContentType.objects.get_for_model(
                AllTimeDiscount),
            object_id=all_disct.pk
        )

    def test_login(self):
        user_login = self.client.login(username="admin", password="123")
        self.assertTrue(user_login)
        response = self.client.get("/orders/")
        self.assertEqual(response.status_code, 200)

    def test_order_str(self):
        obj = models.Order.objects.all().first()
        self.assertTrue(obj.__str__())

    def test_product_str(self):
        obj = models.Product.objects.all().first()
        self.assertTrue(obj.__str__())

    def test_product_get_all_discount(self):
        self.create_object_sale()
        obj = models.Product.objects.all().first()
        self.assertTrue(obj.get_all_discount())

    def test_product_get_all_discount_none(self):
        obj = models.Product.objects.all().first()
        self.assertFalse(obj.get_all_discount())

    def test_product_price(self):
        self.create_object_sale()
        obj = models.Product.objects.all().first()
        self.assertNotEqual(obj.price, obj.start_price)

    def test_sale_discount(self):
        self.create_object_sale()
        obj = Sale.objects.all().first()
        self.assertTrue(obj.discount)

    def test_sale_str(self):
        self.create_object_sale()
        obj = Sale.objects.all().first()
        self.assertTrue(obj.__str__())
