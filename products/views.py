from django.shortcuts import render, redirect
# make sure user is login to create page
from django.contrib.auth.decorators import login_required
from .models import Products
from django.utils import timezone


def home(request):
    return render(request, 'products/home.html')


@login_required
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
            return redirect('home')
        else:
            return render(request, 'products/create.html', {'error': 'All fields required.'})

    else:
        return render(request, 'products/create.html',)
