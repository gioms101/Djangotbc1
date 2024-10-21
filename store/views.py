from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Category, Product
from django.core.paginator import Paginator
from django.db.models import Min, Max, Avg, Sum, F


# Create your views here.


def about(request):
    return HttpResponse("About Store App")


def categories(request):
    category_set = Category.objects.all()
    returning_value = []
    for category in category_set:
        returning_value.append({
            'name': category.name,
            "parend_id": category.parent_id,
            "parent_name": category.parent.name if category.parent_id else None
        })
    return JsonResponse(returning_value, safe=False)


def product_list(request):
    products = Product.objects.all()
    returning_value = []
    for product in products:
        returning_value.append({
            "name": product.name,
            "category_name": [category.name for category in product.category.all()],
            "image": product.image.url if product.image else None
        })
    return JsonResponse(returning_value, safe=False)


def product_listing(request, category_id):
    products = Product.objects.filter(category__id=category_id).annotate(total_price=F('price') * F('quantity'))
    statistic_of_products = products.aggregate(most_expensive=Max('price'),
                                               cheapest=Min('price'),
                                               avg=Avg('price'),
                                               total=Sum('total_price'))

    paginator = Paginator(products, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'statistic_of_products': statistic_of_products
    }
    return render(request, 'product_listing.html', context)


def products_detailed_page(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        "product": product,
    }
    return render(request, 'product_detailed_page.html', context)


def main_page(request):
    current_page = 'main_page'
    products = Product.objects.prefetch_related('category')
    return render(request, 'index.html', {'products': products, 'current_page': current_page})


def category_page(request, slug=None):
    current_page = 'category_page'
    products = Product.objects.prefetch_related('category')

    # 'categories' for category_fragment.html
    categories = Category.objects.prefetch_related('product_set')

    return render(request, 'shop.html', {'products': products, "categories": categories, 'current_page': current_page})


def shop_detail(request, slug=None):
    current_page = 'shop_detail'
    if slug:
        product = Product.objects.get(name=slug)
    else:
        product = Product.objects.first()

    # 'categories' for category_fragment.html
    categories = Category.objects.prefetch_related('product_set')

    # 'products' for featured_products_fragment.html and scroll_products_fragment.html
    products = Product.objects.prefetch_related('category')

    return render(request, 'shop-detail.html', {'product': product, 'categories': categories,
                                                'products': products, 'current_page': current_page
                                                })


def cart_page(request):
    return render(request, 'cart.html')


def checkout_page(request):
    return render(request, 'chackout.html')


def contact_page(request):
    current_page = 'contact_page'
    return render(request, 'contact.html', {'current_page': current_page})
