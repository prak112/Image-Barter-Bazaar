from django.contrib import admin

from photostore.models import Customer, Product, Order, OrderDetail

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderDetail)