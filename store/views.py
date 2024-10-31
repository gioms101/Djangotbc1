from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from .models import Category, Product, ProductTag
from order.models import CartItem
from user.models import CustomUser
from user.forms import RegisterUserForm


# Create your views here.

class MainPage(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'
    queryset = Product.objects.join_related_tables()  # join_related_tables()  is custom method in managers.py
    paginate_by = 3


class CategoryPage(ListView):
    model = Product
    template_name = 'shop.html'
    context_object_name = 'products'
    queryset = Product.objects.join_related_tables()
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        searched = self.request.GET.get('searched')
        sorting_field = self.request.GET.get('sorting_products')
        slug = self.kwargs.get('slug')
        price = self.request.GET.get('rangeInput')
        product_tag = self.request.GET.get('product_tag')

        if slug:
            queryset = queryset.filter(category__name=slug)

        if price and price != '0':
            queryset = queryset.filter(price__lte=price)

        if product_tag:
            queryset = queryset.filter(tags__name=product_tag)

        elif searched:
            queryset = queryset.filter(name__contains=searched)
        elif sorting_field:
            queryset = queryset.order_by(sorting_field)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slug'] = self.kwargs.get('slug') or ''
        context['tags'] = ProductTag.objects.all()
        context['categories'] = Category.objects.filter(parent__name=context['slug'])
        return context

    def post(self, request, *args, **kwargs):  # invokes pre_save() signal to check product quantity in signals.py
        # handle product add to cart in POST request
        product_id = request.POST.get('product')
        cart_id = request.POST.get('cart')
        if product_id and cart_id:
            CartItem.objects.create(cart_id=cart_id, product_id=product_id)

        return self.get(request, *args, **kwargs)


class RegisterPage(CreateView):
    model = CustomUser
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('store:category')

    def form_valid(self, form):
        response = super().form_valid(form)

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)

        if user:
            login(self.request, user)

        return response


class ContactView(TemplateView):
    template_name = 'contact.html'

# momavalshi sheidzleba damchirdes amitom ar wavshli
# def shop_detail(request, slug=None):
#     current_page = 'shop_detail'
#     if slug:
#         product = Product.objects.get(name=slug)
#     else:
#         product = Product.objects.first()
#
#     # 'categories' for category_fragment.html
#     categories = Category.objects.prefetch_related('product_set')
#
#     # 'products' for featured_products_fragment.html and scroll_products_fragment.html
#     products = Product.objects.prefetch_related('category')
#
#     return render(request, 'shop-detail.html', {'product': product, 'categories': categories,
#                                                 'products': products, 'current_page': current_page
#                                                 })
# def checkout_page(request):
#     return render(request, 'chackout.html')
