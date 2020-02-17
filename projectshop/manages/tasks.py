from math import sqrt
from projectshop.celery import app

import datetime

from manages.models import Product, Sale


@app.task(name="manages.tasks.square_root")
def square_root(value):
    print('YES SQUARE_ROOT')
    return sqrt(value)


@app.task(name="manages.tasks.product_all")
def product_all():
    status = ''       # if need delete all sales change this value to 'clear'

    objs = Product.objects.all()
    sale_obj, created = Sale.objects.get_or_create(
        name='Classic time-product sale', discount=20
    )

    for obj in objs:
        value = datetime.datetime.now(datetime.timezone.utc).date() - obj.create_date
        if datetime.timedelta(30)<=value and not obj.sale.all() and status!='clear' :
            obj.sale.add(sale_obj)
            obj.save()
        elif status == 'clear':
            obj.sale.clear()
            obj.save()

    print('Complete run')

