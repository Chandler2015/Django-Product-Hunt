from django.contrib import admin
from .models import Products


class ProductsAdmin(admin.ModelAdmin):

    list_display = ['title', 'summary', 'pub_date_pretty']


admin.site.register(Products, ProductsAdmin)
