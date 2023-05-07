from django.contrib import admin
from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Review)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Order)
class ProductAdmin(admin.ModelAdmin):
    list_display = []

@admin.register(OrderItem)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(ShippingAddress)
class ProductAdmin(admin.ModelAdmin):
    list_display = []
    