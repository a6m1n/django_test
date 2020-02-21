"""Celery tasks file"""
import datetime

from django.contrib.contenttypes.models import ContentType

from projectshop.celery import app
from manages.models import Product
from sales.models import AllTimeDiscount, Sale


@app.task(name="manages.tasks.product_all")
def product_all(status: str = None):
    """Adds sale with percent 20 to all product, that were created before
     30 days. If status = "clear" celery task will remove all sale in products

    # if need delete all sales change this value to 'clear'
    status = None
    status = 'clear' - delete all sale
    """

    product_objs = Product.objects.all()
    time_sale, created = AllTimeDiscount.objects.get_or_create(
        name="Classic time-product sale", discount=20
    )

    for prod_obj in product_objs:
        current_date = datetime.datetime.now(datetime.timezone.utc).date()

        value = current_date - prod_obj.create_date
        is_over_days = datetime.timedelta(30) <= value
        if is_over_days and not prod_obj.sales.all() and status != "clear":
            Sale.objects.create(
                name="Classic all-time sale",
                product=prod_obj,
                content_type=ContentType.objects.get_for_model(
                    AllTimeDiscount),
                object_id=time_sale.pk
            )
        elif status == "clear":
            prod_obj.sales.all().delete()
            prod_obj.save()

    print("Complete run! #file celery tasks")
