from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    sale = models.ForeignKey('Sale', on_delete=models.CASCADE, blank=True, null=True,)
    create_date = models.DateField()

    def new_price(self):
        if self.sale:
            return (self.price*self.sale.discount)/100
        return ''

    def __str__(self):
        return f'{self.name} {self.price} ({self.id})'

class Order(models.Model):
    STATUSES = [
        ('N', 'New'),
        ('D', 'Done'),
        ('P', 'payed'),
    ]
    product = models.OneToOneField(Product, on_delete=models.CASCADE,)
    client_phone_number = models.CharField(max_length=30)
    status = models.CharField(max_length=1, choices=STATUSES, default='N',)

    def __str__(self):
        return f'{self.product.name} {self.get_status_display()} ({self.id})'

class Sale(models.Model):
    discount = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return f'{self.discount} ({self.id})'