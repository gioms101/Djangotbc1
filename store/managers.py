from django.db import models


class ProductManager(models.Manager):
    def join_related_tables(self):
        return self.prefetch_related('category').prefetch_related('tags')


class CartItemManager(models.Manager):
    def join_related_tables(self):
        return self.select_related('cart').select_related('product')
