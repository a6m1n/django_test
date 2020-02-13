from django.core.validators import MaxValueValidator
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    start_price = models.DecimalField(max_digits=5, decimal_places=2)
    sale = models.ManyToManyField('Sale', blank=True)
    create_date = models.DateField()

    def get_all_discount(self):
        summ = sum(self.sale.all().values_list('discount', flat=True))
        return summ if summ<=100 else 99

    @property
    def price(self):
        if self.sale.all():
            return round(self.start_price - (self.start_price*self.get_all_discount()/100), 2)
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
    date_create_order = models.DateTimeField(auto_now_add=True)
    date_close_order = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.product.name} {self.get_status_display()} ({self.pk})'


class Sale(models.Model):
    name = models.CharField(max_length=255)
    discount = models.PositiveIntegerField(unique=True, validators=[MaxValueValidator(100)])
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()

    def __str__(self):
        return f'{self.discount} ({self.pk})'
