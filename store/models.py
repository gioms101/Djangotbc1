from django.db import models
from order.models import UserCard
from .managers import ProductManager, CartItemManager


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(to='Category', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class ProductTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.ManyToManyField(Category, blank=True)
    image = models.ImageField(upload_to='products/', default='default.png')
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    tags = models.ManyToManyField(ProductTag, blank=True)

    def __str__(self):
        return self.name

    objects = ProductManager()


class CartItem(models.Model):
    cart = models.ForeignKey(UserCard, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'Item of {self.cart}'

    objects = CartItemManager()
