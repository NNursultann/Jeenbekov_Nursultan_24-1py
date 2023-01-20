from django.shortcuts import render
from product.models import Product, Review

# Create your views here.

def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        context = {
            'products': products
        }

        return render(request, 'products/products.html', context=context)

def product_detail_view(request, id):
    if request.method == 'GET':
        product_obj = Product.objects.get(id=id)
        review =Review.objects.filter(product=product_obj)
        context = {
            'products': product_obj,
            'review': review
        }

        return render(request, 'products/detail.html', context=context)