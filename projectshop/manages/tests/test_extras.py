"""Test template custom filter who added to query GET request page
and num page. Need this in filter orders django"""
from django.test import TestCase
from django.test.client import Client
from manages.templatetags import manages_extras


class TestExtrasDjangoClass(TestCase):
    """Test django template tag"""

    def setUp(self):
        self.client = Client()

    def test_func_extras(self):
        """     add to url request pagination query params and return new url
        input_data:


                    first param: '/product/?status=New' #url in context
                    second_param: page=1

            output_data = '/product/?status=New&page=1'
        """
        response = self.client.get('/products/?status=New&date_start=01-01-2010')

        result_function_extras_change_url = manages_extras.query_transform(
            response.context, page="1"
        )

        will_result_sting = "status=New&date_start=01-01-2010&page=1"

        assert will_result_sting == result_function_extras_change_url
