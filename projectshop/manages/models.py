from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from datetime import datetime, timezone

from sales.models import (
    AllTimeDiscount, PromoCodeDiscount, StorageDiscount, TemporaryDiscount
)


class Product(models.Model):
    name = models.CharField(max_length=255)
    start_price = models.DecimalField(max_digits=7, decimal_places=2)
    sale = models.ForeignKey(
        'Sale', blank=True, null=True, on_delete=models.CASCADE
    )
    create_date = models.DateField()

    @property
    def price(self):
        if self.sale:
            return round(self.start_price -
                         (self.start_price*self.sale.discount/100), 2)
        return self.start_price

    def __str__(self):
        return f'{self.name} {self.price} ({self.pk})'


class Order(models.Model):
    STATUSES = [
        ('N', 'New'),
        ('D', 'Done'),
        ('P', 'Payed'),
    ]
    product = models.OneToOneField(Product, on_delete=models.CASCADE,)
    client_phone_number = models.CharField(max_length=30)
    status = models.CharField(max_length=1, choices=STATUSES, default='N',)
    date_create_order = models.DateField()
    date_close_order = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.product.name} {self.get_status_display()} ({self.pk})'


class Sale(models.Model):
    name = models.CharField(max_length=255)
    date_create = models.DateTimeField(blank=True, null=True)

    storage_dsc = GenericRelation(StorageDiscount)
    all_time_dsc = GenericRelation(AllTimeDiscount)
    temporary_dsc = GenericRelation(TemporaryDiscount)
    promo_code_dsc = GenericRelation(PromoCodeDiscount)

    @property
    def discount(self):
        return self.get_all_discount()

    def get_all_discount(self):
        total_sum_discount = 0
        lists_var = [
            "storage_dsc", "all_time_dsc", "temporary_dsc", "promo_code_dsc"
        ]

        for attr in lists_var:
            total_sum_discount += sum(
                getattr(self, attr).all().values_list('discount', flat=True))

        return total_sum_discount if total_sum_discount <= 100 else 99

    def __str__(self):
        return f'Name discount: "{self.name}". Percent discount: {self.discount}%. (ID:{self.pk})'
