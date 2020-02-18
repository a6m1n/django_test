""" Django view file. Check urls.py """

from datetime import datetime

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView, UpdateView
from django.views.generic.detail import DetailView
from django.shortcuts import redirect
from django.db.models import Q


from .models import Product, Order
from .forms import ProductForm, OrderForm


class IndexView(TemplateView):
    """
    Index template.
    All info for our site need add to manages/index.html
    This template user sees first
    """

    template_name = "manages/index.html"


class ProductListView(ListView):
    """
    View product in table.
    """

    model = Product
    context_object_name = "products"
    template_name = "manages/product_list.html"
    paginate_by = 10


class ProductDetailView(DetailView):
    """
    View detail product.
    url: host/products/1      # 1 - example id product
    """

    model = Product
    template_name = "manages/product_detail.html"
    context_object_name = "product"


class CreateProductView(FormView):
    """
    Create product in HTML template.
    url: host/products/create
    """

    template_name = "manages/product_create.html"
    form_class = ProductForm
    success_url = "/products/"

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        return self.form_invalid(form)


class OrdersListView(ListView):
    """ List view who have custom filter """
    model = Order
    context_object_name = "orders"
    template_name = "manages/order_list.html"
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        status = self.request.GET.get("status")
        date_create_order = self.request.GET.get("date_start")
        date_close_order = self.request.GET.get("date_end")
        object_q = Q()

        if status:
            object_q &= Q(status=status[0])

        if date_close_order:
            date_object_close = datetime.strptime(
                date_close_order, "%d-%m-%Y"
            ).date()

            object_q &= Q(date_close_order__gte=date_object_close)

        if date_create_order:
            date_object_create = datetime.strptime(
                date_create_order, "%d-%m-%Y"
            ).date()

            object_q &= Q(date_create_order__gte=date_object_create)
            # q &= Q(date_create_order__year__gte=2000)

        return super().get_queryset(*args, **kwargs).filter(object_q)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["status"] = Order.STATUSES
        return context


class CreateOrderView(FormView):
    """
    Create product in HTML template.
    url: host/orders/create
    """

    template_name = "manages/order_create.html"
    form_class = OrderForm
    success_url = "/orders/"

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        return self.form_invalid(form)


class OrderDetailView(DetailView):
    """
    View detail order.
    url: host/order/1      # 1 - example id product
    """

    model = Order
    context_object_name = "order"
    template_name = "manages/order_detail.html"


class OrderUpdate(UpdateView):
    """Update order view"""
    model = Order
    template_name_suffix = "_update_form"
    fields = ["product", "client_phone_number", "status", "date_create_order"]

    def get_success_url(self):
        order_id = self.kwargs["pk"]
        return reverse_lazy("order_detail", kwargs={"pk": order_id})


class GenerateCheckView(DetailView):
    """A base view for displaying a single object."""

    model = Order
    context_object_name = "order"
    template_name = "manages/order_generate.html"

    def post(self, request, pimarykey, *args, **kwargs):
        """Classic post request"""
        super().get(request, *args, **kwargs)
        return redirect(reverse_lazy(
            "check_complete", kwargs={"pk": pimarykey})
        )


class SuccessOrderView(DetailView):
    """
    View who shows data from success order and change order status to payed
    and change field close order
    """

    model = Order
    context_object_name = "order"
    template_name = "manages/success_order.html"

    def get(self, request, *args, **kwargs):
        resp = super().get(request, *args, **kwargs)
        if self.object.status == "D":
            self.object.status = "P"
            self.object.date_close_order = datetime.now().date()
            self.object.save()
            return resp
        return HttpResponse("Error")


class ErrorView404(TemplateView):
    """
    Error views.
    This view is needed to display errors.
    There are no details, only wishes to contact the cashier to find
    out the error
    """

    template_name = "manages/error.html"
