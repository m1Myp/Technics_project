from django.urls import path, include
from rest_framework import routers
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from .models import Info
from .serializers import Product_serializer

# router = routers.DefaultRouter()
# router.register(r'test', views.ProductsViewSet)
# router.register(r'product//', views.ProductDetail.as_view())

urlpatterns = [
    path('', views.index, name='index'),
    path('scrap_all', views.scrap_all, name='scrap_all'),
    path('api/v1/test/', views.ProductList.as_view()),
    path('api/v1/product/<int:product_id>', views.view_product_by_id, name='product_detail'),
    path('api/v1/c=<slug:category>', views.view_with_filter),
    path('api/v1/c=<slug:category>/p=<int:page>', views.view_with_filter),
]

# urlpatterns = format_suffix_patterns(urlpatterns)