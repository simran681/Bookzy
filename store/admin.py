from django.contrib import admin
from . import models


class AdminBook(admin.ModelAdmin):
    list_display = ['name', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name']


# Register your models here.
admin.site.register(models.Book, AdminBook)
admin.site.register(models.Category, AdminCategory)
admin.site.register(models.Customer, AdminCustomer)
