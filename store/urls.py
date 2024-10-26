from django.urls import path
from .views import MainPage, ContactView, CategoryPage, CartPage


app_name = 'store'

urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('category/', CategoryPage.as_view(), name='category'),
    path('category/<slug:slug>', CategoryPage.as_view(), name='specific_category'),
    path('contact/', ContactView.as_view(), name='contact_page'),
    path('order/cart', CartPage.as_view(), name='cart'),
]

# path('order/checkout', views.checkout_page, name='checkout_page'),
# path('product/', views.shop_detail, name='shop_detail'),
# path('product/<slug:slug>', views.shop_detail, name='shop_detail_product'),
