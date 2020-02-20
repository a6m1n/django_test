""" Class run fixtures """
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth.models import User

from manages.models import Product, Order


class Command(BaseCommand):
    """ Class run fixtures """
    help = 'Run custom fixtures edit from this file'

    def handle(self, *args, **options):
        print('Clear table: Product, Order, User\n')
        Product.objects.all().delete()
        Order.objects.all().delete()
        User.objects.all().delete()

        print('Run fixtures\n')
        call_command("loaddata", "data_users.json")
        call_command("loaddata", "data_products.json")
        call_command("loaddata", "data_orders.json")

        print('\nFixtures has loaded')
