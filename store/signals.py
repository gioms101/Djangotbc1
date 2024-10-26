from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.http import Http404

from .models import CartItem, Product


@receiver(pre_save, sender=CartItem)
def check_validity(sender, instance, **kwargs):
    product_obj = Product.objects.get(id=instance.product_id)
    if product_obj.quantity == 0:
        raise Http404("Not Enough Amount to add to cart!")
    else:
        product_obj.quantity -= 1
        product_obj.save()


@receiver(post_delete, sender=CartItem)
def delete_cart_item(sender, instance, **kwargs):
    product_obj = Product.objects.get(id=instance.product_id)
    product_obj.quantity += 1
    product_obj.save()
