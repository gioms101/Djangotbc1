from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from .models import Category, Product, CartItem, ProductTag
from django.core.paginator import Paginator
from django.db.models import Min, Max, Avg, Sum, F


# Create your views here.

def main_page(request):
    products = Product.objects.join_related_tables()

    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'products': page_obj})


def category_page(request, slug=None):

    if request.method == 'POST':
        product = request.POST.get('product')
        cart = request.POST.get('cart')

        # invokes pre_save() signal to check product quantity.
        CartItem.objects.create(cart_id=cart, product_id=product)

    tags = ProductTag.objects.all()

    if slug:
        specific_category = Category.objects.filter(parent__name=slug)
        specific_products = Product.objects.filter(category__name=slug)
        return render(request, 'shop.html', {'products': specific_products, 'tags': tags, 'slug': slug,
                                             "categories": specific_category})
    # 'categories' for category_fragment.html
    categories = Category.objects.filter(parent_id=None).prefetch_related('product_set')

    if 'rangeInput' in request.GET:
        if 'product_tag' in request.GET:
            tag = request.GET['product_tag']
            num = request.GET['rangeInput']

            filtered_products = Product.objects.filter(tags__name=tag).filter(price__lte=num) if num != '0' else (
                Product.objects.filter(tags__name=tag))

            return render(request, 'shop.html', {'products': filtered_products, 'tags': tags,
                                                 "categories": categories})
        else:
            num = request.GET['rangeInput']
            filtered_product = Product.objects.filter(price__lte=num)
            return render(request, 'shop.html', {'products': filtered_product, 'tags': tags,
                                                 "categories": categories})

    elif 'searched' in request.GET:
        searched = request.GET['searched']
        searched_product = Product.objects.filter(name__contains=searched)
        return render(request, 'shop.html', {'products': searched_product, 'tags': tags,
                                             "categories": categories})

    elif 'sorting_products' in request.GET:
        sorting_field = request.GET['sorting_products']
        sorted_products = Product.objects.order_by(sorting_field)

        return render(request, 'shop.html', {'products': sorted_products, 'tags': tags,
                                             "categories": categories})

    else:
        products = Product.objects.join_related_tables()

        # for pagination
        paginator = Paginator(products, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'shop.html', {'products': page_obj, 'tags': tags,
                                             "categories": categories})


def contact_page(request):
    return render(request, 'contact.html')



# momavalshi sheidzleba damchirdes amitom ar wavshli

# def about(request):
#     return HttpResponse("About Store App")
#
#
# def categories(request):
#     category_set = Category.objects.all()
#     returning_value = []
#     for category in category_set:
#         returning_value.append({
#             'name': category.name,
#             "parend_id": category.parent_id,
#             "parent_name": category.parent.name if category.parent_id else None
#         })
#     return JsonResponse(returning_value, safe=False)
#
#
# def product_list(request):
#     products = Product.objects.all()
#     returning_value = []
#     for product in products:
#         returning_value.append({
#             "name": product.name,
#             "category_name": [category.name for category in product.category.all()],
#             "image": product.image.url if product.image else None
#         })
#     return JsonResponse(returning_value, safe=False)
#
#
# def product_listing(request, category_id):
#     products = Product.objects.filter(category__id=category_id).annotate(total_price=F('price') * F('quantity'))
#     statistic_of_products = products.aggregate(most_expensive=Max('price'),
#                                                cheapest=Min('price'),
#                                                avg=Avg('price'),
#                                                total=Sum('total_price'))
#
#     paginator = Paginator(products, 1)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     context = {
#         'page_obj': page_obj,
#         'statistic_of_products': statistic_of_products
#     }
#     return render(request, 'product_listing.html', context)
#
#
# def products_detailed_page(request, product_id):
#     product = Product.objects.get(id=product_id)
#     context = {
#         "product": product,
#     }
#     return render(request, 'product_detailed_page.html', context)

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


# def cart_page(request):
#     return render(request, 'cart.html')


# def checkout_page(request):
#     return render(request, 'chackout.html')
