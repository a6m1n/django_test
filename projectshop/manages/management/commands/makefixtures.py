""" Make fixtures command """
from django.core.management.base import BaseCommand
import manages.fixtures.create_fixtures as fixtures


class Command(BaseCommand):
    """Class makefixtures"""
    help = 'Make fixtures files'

    def handle(self, *args, **options):
        fixtures.main()
