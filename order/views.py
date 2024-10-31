
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CartItem

# Create your views here.


"""If you click the Cart symbol on the navbar, CartPage view will display order items, where you 
can delete some of the orders."""


class CartPage(LoginRequiredMixin, ListView):
    model = CartItem
    template_name = 'cart.html'
    context_object_name = 'ordered_products'

    def get_queryset(self):
        return CartItem.objects.join_related_tables().filter(cart_id=self.request.user.id)

    def post(self, request, *args, **kwargs):
        deleting_item_id = request.POST.get('deleting_item')
        cart_item = CartItem.objects.get(id=deleting_item_id)
        cart_item.delete()  # invokes post_delete signal to upgrade product quantity in signals.py

        return self.get(request, *args, **kwargs)
