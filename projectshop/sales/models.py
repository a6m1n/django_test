"""Models sales """
from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey

from manages.models import Product

from typing import Any, Optional

class Sale(models.Model):
    """"Model Sale"""
    name = models.CharField(max_length=255)
    date_create = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        related_name='sales',
        blank=True,
        null=True,
    )

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    @property
    def discount(self) -> Optional[Any]:
        """"discount one object"""
        return self.content_object.discount

    def __str__(self):
        return f"Name : {self.name}. Percent: {self.discount}%. (ID:{self.pk})"


class DefineModelDiscount(models.Model):
    """ define model discount """

    name = models.CharField(max_length=255)
    discount = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    tags = GenericRelation(Sale, related_query_name="sale")

    def __str__(self):
        return f"Id: {self.pk}. Percent: {self.discount}% ."

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
