from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('categories_list/', views.categories, name='categories_list'),
    path('product-list/', views.product_list, name='product-list'),
    path('category/', views.category, name='category'),
    path('category/<int:category_id>/products/', views.product_listing, name='product_listing'),
    path('products/<int:product_id>/detailed/', views.products_detailed_page, name='detailed_page'),
]

