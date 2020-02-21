""""Django models from app manages"""
from django.db import models


class Product(models.Model):
    """ Model Product """
    name = models.CharField(max_length=255)
    start_price = models.DecimalField(
        max_digits=7, decimal_places=2
    )
    create_date = models.DateField()

    def get_all_discount(self):
        """ Returned total discount """
        result = 0
        sales = self.sales.all()
        for sale in sales:
            result += sale.content_object.discount
        return result if result <= 100 else 99

    @property
    def price(self):
        """" Property method who returned current price product """
        if self.sales.all():
            percent_sale = self.start_price * self.get_all_discount() / 100
            return round(self.start_price-percent_sale, 2)
        return self.start_price

    def __str__(self):
        return f'{self.name} {self.price} ({self.pk})'


class Order(models.Model):
    """ Model Order """
    STATUSES = [
        ("N", "New"),
        ("D", "Done"),
        ("P", "Payed"),
    ]
    product = models.OneToOneField(Product, on_delete=models.CASCADE,)
    client_phone_number = models.CharField(max_length=30)
    status = models.CharField(max_length=1, choices=STATUSES, default="N",)
    date_create_order = models.DateField()
    date_close_order = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.product.name} {self.get_status_display()} ({self.pk})"
