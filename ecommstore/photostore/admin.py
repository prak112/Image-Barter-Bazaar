from django.contrib import admin

from photostore.models import Customers, Products, Orders, OrderDetails

# Register your models here.
admin.site.register(Customers)
admin.site.register(Products)
admin.site.register(Orders)
admin.site.register(OrderDetails)