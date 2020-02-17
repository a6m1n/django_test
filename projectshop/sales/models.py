from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType



class DefineModelDiscount(models.Model):
    """ define model discount """
    name = models.CharField(max_length=255)
    discount = models.PositiveIntegerField(validators=[MaxValueValidator(100)])

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f'Name: {self.__class__.__name__}. Percent: {self.discount}% .'

    class Meta:
        abstract = True


class TemporaryDiscount(DefineModelDiscount):
    date_start_discount = models.DateField()
    date_close_discount = models.DateField()


class AllTimeDiscount(DefineModelDiscount):
    pass


class StorageDiscount(DefineModelDiscount):
    """
    Accumulative Discount

    """
    pass


class PromoCodeDiscount(DefineModelDiscount):
    code = models.CharField(max_length=30)


