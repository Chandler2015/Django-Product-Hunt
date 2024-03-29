from django.shortcuts import render, redirect, get_object_or_404
# make sure user is login to create page
from django.contrib.auth.decorators import login_required
from .models import Products
from django.utils import timezone


def home(request):
    products = Products.objects
    return render(request, 'products/home.html', {'products': products})


@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product = Products()
            product.title = request.POST['title']
            product.body = request.POST['body']
            product.url = request.POST['url']
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.pub_date = timezone.datetime.now()
            product.hunter = request.user
            product.save()
            return redirect('/products/'+str(product.id))
        else:
            return render(request, 'products/create.html', {'error': 'All fields required.'})

    else:
        return render(request, 'products/create.html',)


def detail(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    return render(request, 'products/detail.html', {'product': product})


@login_required(login_url="/accounts/signup")
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Products, pk=product_id)
        product.votes_total += 1
        product.save()
        return redirect('/products/'+str(product.id))
