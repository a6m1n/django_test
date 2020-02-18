"""Models sales (custom name this app: saleiki :D)"""
from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.contenttypes.fields import GenericRelation

from manages.models import Sale


class DefineModelDiscount(models.Model):
    """ define model discount """

    name = models.CharField(max_length=255)
    discount = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    tags = GenericRelation(Sale, related_query_name="sale")

    def __str__(self):
        return f"Name: {self.__class__.__name__}. Percent: {self.discount}% ."

    class Meta:
        abstract = True


class TemporaryDiscount(DefineModelDiscount):
    """ Temp discount model """
    date_start_discount = models.DateField()
    date_close_discount = models.DateField()


class AllTimeDiscount(DefineModelDiscount):
    """ Simple model discount to all time"""
    pass


class StorageDiscount(DefineModelDiscount):
    """Accumulative Discount"""
    is_active_user = models.BooleanField(default=True)


class PromoCodeDiscount(DefineModelDiscount):
    """ model promocode discount """
    code = models.CharField(max_length=30)
