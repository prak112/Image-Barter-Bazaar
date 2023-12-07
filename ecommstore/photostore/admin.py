from django.contrib import admin

from photostore.models import Customer, Product, Order, Cart

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
#admin.site.register(OrderDetail)