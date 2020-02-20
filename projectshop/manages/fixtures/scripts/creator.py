"""Module with classes to create fixtures to django"""
import random
import json

from manages.fixtures.scripts.utils import random_datetime, generate_phone


class CreateFixtureProduct:
    """Class creator fixture to product """
    def __init__(self):
        self.app = "manages"
        self.model = "product"
        self.path = "manages/fixtures/"
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

    def create_data(self):
        """Creation all fixtures data"""

        for primary_key in range(1, 100):
            new_dict = {}
            new_dict["model"] = f"{self.app}.{self.model}"
            new_dict["pk"] = primary_key
            new_dict["fields"] = {}

            new_dict["fields"]["name"] = random.choice(self.names)
            new_dict["fields"]["start_price"] = random.randint(1, 3000)
            new_dict["fields"]["create_date"] = (
                random_datetime().date().isoformat()
            )

            self.data.append(new_dict)

    def write_to_file(self, name_file):
        """Write to file json data"""
        with open(self.path + name_file, "w", encoding="utf-8") as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)
        return True


class CreateFixtureOrder(CreateFixtureProduct):
    """Class creator fixtures to model manages.Order"""
    def __init__(self):
        self.statuses = [
            ("N", "New"),
            ("D", "Done"),
            ("P", "Payed"),
        ]
        self.app = "manages"
        self.model = "order"
        self.path = 'manages/fixtures/'
        self.array_id_proudct = [id_product for id_product in range(1, 100)]
        self.data = []

    def generate_statuse(self):
        """Returned random status from self.statuses """
        return random.choice(self.statuses)[0]

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
            new_dict["fields"]["client_phone_number"] = generate_phone()
            new_dict["fields"]["status"] = self.generate_statuse()
            new_dict["fields"]["date_create_order"] = (
                random_datetime().date().isoformat()
            )

            self.data.append(new_dict)
