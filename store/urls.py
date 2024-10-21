from django.urls import path
from . import views


app_name = 'store'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('category/', views.category_page, name='category'),
    path('category/<slug:slug>', views.category_page, name='specific_category'),
    path('product/', views.shop_detail, name='shop_detail'),
    path('product/<slug:slug>', views.shop_detail, name='shop_detail_product'),
    path('order/cart', views.cart_page, name='cart'),
    path('order/checkout', views.checkout_page, name='checkout_page'),
    path('contact/', views.contact_page, name='contact_page'),
    path('about/', views.about, name='about'),
    path('categories_list/', views.categories, name='categories_list'),
    path('product-list/', views.product_list, name='product-list'),
    path('category/<int:category_id>/products/', views.product_listing, name='product_listing'),
    path('products/<int:product_id>/detailed/', views.products_detailed_page, name='detailed_page'),
]

