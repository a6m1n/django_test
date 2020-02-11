from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from .models import Product

class IndexView(TemplateView):
    template_name = "manages/index.html"

class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'manages/product_list.html'
    paginate_by = 10

class ProductDetailView(DetailView):
    model = Product
    template_name = 'manages/product_detail.html'
    context_object_name = 'product'