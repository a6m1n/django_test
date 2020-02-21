"""This file testing only CELERY job IN DJANGO PROJ!"""

from django.test import TransactionTestCase
from celery.contrib.testing.worker import start_worker
from manages import tasks
from sales.models import Sale

from projectshop.celery import app


class CeleryTests(TransactionTestCase):
    """ This class testing one task celery, and adding fixtures """

    fixtures = ['data_products.json', 'data_orders.json']

    @classmethod
    def setUpClass(cls):
        @app.task(name='celery.ping')
        def ping():
            return 'pong'

        super().setUpClass()

        cls.celery_worker = start_worker(app)
        cls.celery_worker.__enter__()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.celery_worker.__exit__(None, None, None)

    def test_add_sale_from_celery(self):
        """Run celery task who added sale to all product where:
         date < date_create_product - 30days
         """
        task = tasks.product_all.delay()
        task.get(timeout=15)

        self.assertNotEqual(len(Sale.objects.all()), 0)
        assert task.state == "SUCCESS"

    def test_clear_sale_from_celery(self):
        """ Run celery task who clear all sale from products! """
        task = tasks.product_all.delay(status='clear')
        task.get(timeout=15)

        self.assertEqual(len(Sale.objects.all()), 0)
        assert task.state == "SUCCESS"
