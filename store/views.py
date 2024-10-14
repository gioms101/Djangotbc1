from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Category, Product
from django.core.paginator import Paginator
from django.db.models import Min, Max, Avg, Sum, F


# Create your views here.

def index(request):
    return HttpResponse("Store App")


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


def category(request):
    parent_categories = Category.objects.filter(parent_id=None).prefetch_related('product_set')

    context = {
        "parent_categories": parent_categories
    }

    return render(request, 'category.html', context)


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
