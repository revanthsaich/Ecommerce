from django.urls import path
from . import views
from .views import ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('featured/', views.get_featured_products, name='get_featured_products'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
]
