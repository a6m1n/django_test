""" Define register to django admin sales models"""
from django.contrib import admin
from . import models


admin.site.register(models.TemporaryDiscount)
admin.site.register(models.AllTimeDiscount)
admin.site.register(models.StorageDiscount)
admin.site.register(models.PromoCodeDiscount)
