from django.shortcuts import render, redirect
from product.models import Product, Review
from product.forms import ProductCreateForm, ReviewCreateForm

# Create your views here.

PAGINATION_LIMIT = 3

def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        if search is not None:
            products = Product.objects.filter(name__icontains=search)

        max_page = products.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        products = products[PAGINATION_LIMIT * (page - 1): PAGINATION_LIMIT * page]

        context = {
            'products': products,
            'user': request.user,
            'max_page': range(1, max_page+1)
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
                author_id=request.user.id,
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
                author_id=request.user.id,
                name=form.cleaned_data.get('name'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data.get('price'),
                rate=form.cleaned_data['rate'] if form.cleaned_data['rate'] is not None else 0
            )
            return redirect('/products/')
        return render(request, 'products/create.html', context={
            'form': form
        })