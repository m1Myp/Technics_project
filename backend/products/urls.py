from django.urls import path, re_path

from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('bug_report', views.bug_report),
    path('clean', views.clean, name='clean_db'),
    path('scrap_all', views.scrap_all, name='scrap_all'),
    path('api/v1/test/', views.ProductList.as_view()),
    path('api/v1/product/<int:product_id>', views.view_product_by_id, name='product_detail'),
    path('api/v1/c=<slug:category>', views.view_default),
    path('api/v1/c=<slug:category>/p=<int:page>', views.view_with_filter),
    path('api/v1/c=<slug:category>/p=<int:page>&sorting=<slug:sorting_type>', views.view_with_filter_and_sort),
    path('api/v1/q=<str:search_query>', views.view_with_search),
    path('api/v1/q=<str:search_query>/p=<int:page>&sorting=<slug:sorting_type>', views.view_with_search_page_sort),
]
