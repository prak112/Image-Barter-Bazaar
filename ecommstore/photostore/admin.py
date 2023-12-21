from django.contrib import admin
from photostore.models import Customer, Product, Order, Cart

# imports for redirecting url
from django.utils.http import urlencode
from django.urls import reverse
from django.utils.html import format_html



# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("full_name", "customer_type")
    list_filter = ("customer_type", )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "theme", "category")
    list_display_links = ("title", )
    list_filter = ("category", "theme", "author", )
    search_fields = ("title__icontains", )

    # def view_image_link(self, obj):



@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("view_customer_link", "item", "quantity", )
    # list_display_links = None
    list_filter = ("item__title", )

    def view_customer_link(self, obj):
        url = (
            reverse('admin:photostore_customer_changelist')
            + "?"
            + urlencode({"customer_type": f"{obj.customer_info.customer_type}"})
        )
        url_text = obj.customer_info.full_name
        return format_html('<a href={}>{}</a>', url, url_text)
    view_customer_link.short_description = "Customer"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("__str__", "view_cart_link", "order_date", "order_status", "payment")
    list_display_links = ("order_date", )
    

    def view_cart_link(self, obj):
        url = (
            reverse('admin:photostore_cart_changelist')
            + "?"
            + urlencode({"item__title":f"{obj.customer_order.item.title}"})
        )        
        return format_html('<a href={}>Show</a>', url)
    view_cart_link.short_description = "Details"
    