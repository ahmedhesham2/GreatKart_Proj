from django.contrib import admin
from django.db import models
from store.models import product


class productAdmin(admin.ModelAdmin):
    list_display = ('product_name','slug', 'price', 'stock', 'category', 'modified_date', 'is_available',)
    prepopulated_fields = {'slug': ('product_name',)}

# Register your models here.
admin.site.register(product,productAdmin)