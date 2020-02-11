from django.urls import path
from manages import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='shop'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('products/<int:pk>', views.ProductDetailView.as_view()),
]
