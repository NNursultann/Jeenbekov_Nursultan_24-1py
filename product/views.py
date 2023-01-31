from django.shortcuts import render, redirect
from product.models import Product, Review
from product.forms import ProductCreateForm, ReviewCreateForm

# Create your views here.

def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        context = {
            'products': products,
            'user': request.user
        }

        return render(request, 'products/products.html', context=context)

def product_detail_view(request, id):
    if request.method == 'GET':
        product_obj = Product.objects.get(id=id)
        reviews = Review.objects.filter(product=product_obj)
        context = {
            'products': product_obj,
            'reviews': reviews,
            'forms': ReviewCreateForm
        }

        return render(request, 'products/detail.html', context=context)

    if request.method == 'POST':
        product_obj = Product.objects.get(id=id)
        reviews = Review.objects.filter(product=product_obj)
        form = ReviewCreateForm(data=request.POST)

        if form.is_valid():
            Review.objects.create(
                product=product_obj,
                text=form.cleaned_data.get('text')
            )
            return redirect(f'/products/{product_obj.id}/')

        return render(request, 'products/detail.html', context={
            'product': product_obj,
            'reviews': reviews,
            'form': form
        })

def create_product_view(request):
    if request.method == 'GET':
        context = {
            'form': ProductCreateForm
        }
        return render(request, 'products/create.html', context=context)
    elif request.user.is_anonymous:
        return redirect('/products')
    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST)

        if form.is_valid():
            Product.objects.create(
                name=form.cleaned_data.get('name'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data.get('price'),
                rate=form.cleaned_data['rate'] if form.cleaned_data['rate'] is not None else 0
            )
            return redirect('/products/')
        return render(request, 'products/create.html', context={
            'form': form
        })