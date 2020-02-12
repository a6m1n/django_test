from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, UpdateView
from django.shortcuts import redirect

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
    context_object_name = 'products'
    template_name = 'manages/product_list.html'
    paginate_by = 10

class ProductDetailView(DetailView):
    """
    View detail product.
    url: host/products/1      # 1 - example id product
    """

    model = Product
    template_name = 'manages/product_detail.html'
    context_object_name = 'product'

class CreateProductView(FormView):
    """
    Create product in HTML template.
    url: host/products/create
    """

    template_name = 'manages/product_create.html'
    form_class = ProductForm
    success_url = '/products/'

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class OrdersListView(ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'manages/order_list.html'
    paginate_by = 10

class CreateOrderView(FormView):
    """
    Create product in HTML template.
    url: host/orders/create
    """

    template_name = 'manages/order_create.html'
    form_class = OrderForm
    success_url = '/orders/'

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class OrderDetailView(DetailView):
    """
    View detail order.
    url: host/order/1      # 1 - example id product
    """

    model = Order
    context_object_name = 'order'
    template_name = 'manages/order_detail.html'


class OrderUpdate(UpdateView):
    model = Order
    template_name_suffix = '_update_form'
    fields = ['product', 'client_phone_number', 'status']

    def get_success_url(self):
        orderid = self.kwargs['pk']
        return reverse_lazy('order_detail', kwargs={'pk': orderid})


class GenerateCheckView(DetailView):
    """A base view for displaying a single object."""

    model = Order
    context_object_name = 'order'
    template_name = 'manages/order_generate.html'

    def post(self, request, pk ,*args, **kwargs):
        if request.POST:
            obj = self.model.objects.filter(id=pk).first()
            obj.status = 'P'
            obj.save()
            return redirect(reverse_lazy('check_complete', kwargs={'pk': pk}))
        return self.get(request, pk, *args, **kwargs)

class test(DetailView):
    """

    """
    model = Order
    context_object_name = 'order'
    template_name = "manages/success_order.html"



