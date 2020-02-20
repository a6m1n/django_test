"""Cool my custom func"""
import random
from random import randrange
from datetime import datetime
from datetime import timedelta


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


def random_datetime():
    """ Returned random date start=date_start end=date_end """

    date_start = datetime.strptime(
        "1/1/2000 12:01 AM", "%m/%d/%Y %I:%M %p"
    )
    date_end = datetime.strptime(
        "1/1/2020 11:59 PM", "%m/%d/%Y %I:%M %p"
    )

    return random_date(date_start, date_end)


def generate_phone():
    """Generate phone from random integer. Len(number)==9"""
    return "+" + "".join([str(random.randint(1, 9)) for i in range(9)])
