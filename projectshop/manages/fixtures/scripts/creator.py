"""Module with classes to create fixtures to django"""
import random
import json
from random import randrange
from datetime import datetime
from datetime import timedelta


class CreateFixtureProduct:
    """Class creator fixture to product """
    def __init__(self):
        self.create_big_data()
        self.app = "manages"
        self.model = "product"

    def create_data(self):

        for primary_key in range(1, 100):
            new_dict = {}
            new_dict["model"] = f"{self.app}.{self.model}"
            new_dict["pk"] = primary_key
            new_dict["fields"] = {}

            new_dict["fields"]["name"] = random.choice(self.names)
            new_dict["fields"]["start_price"] = random.randint(1, 3000)
            new_dict["fields"]["create_date"] = (
                self.random_datetime().date().isoformat()
            )

            self.data.append(new_dict)

    def write_to_file(self):
        """Write to file json data"""
        with open("data_products.json", "w", encoding="utf-8") as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)
        return True

    def create_big_data(self):
        """Create all data to this class"""
        self.data = []

        self.names = [
            "Apple",
            "iPhone 3",
            "iPhone 3",
            "Samsung s10",
            "Lenovo a5",
            "Apple airPods",
            "Nike airMax",
            "Adidas NMD",
            "Redmi X23",
            "Genius mouse",
            "4Tech",
        ]

    def random_datetime(self):
        """ Returned random date start=date_start end=date_end """
        def random_date(start, end):
            """
            This function will return a random datetime between two datetime
            objects.
            """
            delta = end - start
            int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
            random_second = randrange(int_delta)
            return start + timedelta(seconds=random_second)

        date_start = datetime.strptime(
            "1/1/2000 12:01 AM", "%m/%d/%Y %I:%M %p"
        )
        date_end = datetime.strptime(
            "1/1/2020 11:59 PM", "%m/%d/%Y %I:%M %p"
        )

        return random_date(date_start, date_end)


class CreateFixtureOrder(CreateFixtureProduct):
    """Class creator fixtures to model manages.Order"""
    def __init__(self):
        self.STATUSES = [
            ("N", "New"),
            ("D", "Done"),
            ("P", "Payed"),
        ]
        self.create_big_data()
        self.app = "manages"
        self.model = "order"
        self.array_id_proudct = [id_product for id_product in range(1, 100)]

    def write_to_file(self):
        """Write to file json data"""
        with open("data_orders.json", "w", encoding="utf-8") as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)
        return True

    def generate_phone(self):
        """Generate phone from random integer. Len(number)==9"""
        return "+" + "".join([str(random.randint(1, 9)) for i in range(9)])

    def generate_statuse(self):
        """Returned random status from self.statuses """
        return random.choice(self.STATUSES)[0]

    def generate_product(self):
        """ Take random product and after take, delete her in list items
        and returned """
        id_p = random.choice(self.array_id_proudct)
        self.array_id_proudct.remove(id_p)
        return id_p

    def create_data(self):

        for primary_key in range(1, 50):
            new_dict = {}
            new_dict["model"] = f"{self.app}.{self.model}"
            new_dict["pk"] = primary_key
            new_dict["fields"] = {}

            new_dict["fields"]["product"] = self.generate_product()
            new_dict["fields"]["client_phone_number"] = self.generate_phone()
            new_dict["fields"]["status"] = self.generate_statuse()
            new_dict["fields"]["date_create_order"] = (
                self.random_datetime().date().isoformat()
            )

            self.data.append(new_dict)
