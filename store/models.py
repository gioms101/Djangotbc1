from django.db import models



# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(to='Category', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ManyToManyField(Category, blank=True)
    image = models.ImageField(upload_to='products/', default='default.png')
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name
