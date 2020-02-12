from django.urls import path
from manages import views

urlpatterns = [
    # example url: http://domain.com/
    path('', views.IndexView.as_view(), name='index'),

    # example url: http://domain.com/products
    path('products/', views.ProductListView.as_view(), name='products'),

    # example url: http://domain.com/orders
    path('orders/', views.OrdersListView.as_view(), name='orders'),

    # example url: http://domain.com/products/1            # 1 - id product
    path('products/<int:pk>', views.ProductDetailView.as_view()),

    # example url: http://domain.com/orders/1            # 1 - id product
    path('orders/<int:pk>', views.OrderDetailView.as_view(), name='order_detail'),

    # example url: http://domain.com/products/create
    path('orders/create', views.CreateProductView.as_view(), name='create_product'),

    # example url: http://domain.com/products/create
    path('products/create', views.CreateOrderView.as_view(), name='create_order'),

    # example url: http://domain.com/orders/1/change
    path('orders/<int:pk>/change', views.OrderUpdate.as_view(), name='order_update'),

    # example url: http://domain.com/orders/1/check            # 1 - id product
    path('orders/<int:pk>/check', views.GenerateCheckView.as_view(), name='gen_check'),

    # example url: http://domain.com/orders/1/check/complete            # 1 - id product
    path('orders/<int:pk>/check/complete', views.test.as_view(), name='check_complete'),


]
