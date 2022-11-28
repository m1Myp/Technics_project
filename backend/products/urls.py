from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'test', views.ProductsViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('scrap_all', views.scrap_all, name='scrap_all'),
    path('api/v1/', include(router.urls))
]
