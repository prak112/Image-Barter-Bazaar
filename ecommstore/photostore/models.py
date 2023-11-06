from django.db import models

from users.models import UserProfile

# Create your models here.

class Customer(models.Model): 
    user_info = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="user_information")
    fullname = models.CharField('Full Name', max_length=128, unique=True)
    type = models.CharField('Customer Type', max_length=20)

    def save_fullname(self, *args, **kwargs):
        self.fullname = f"{self.user_info.first_name} {self.user_info.last_name}"
        super().save_fullname(*args, **kwargs)

    def save_customerType(self, *args, **kwargs):
        self.type = self.user_info.customer_type
        super().save_customerType(*args, **kwargs)


class Product(models.Model):
    TYPE_CHOICES = [
        ('PH', 'Photo'),
        ('ART', 'Art'),
    ]

    THEME_CHOICES = [
        ('mountain', 'Mountain'),
        ('lake', 'Lake'),
        ('polar', 'Polar'),
        ('forest', 'Forest'),
        ('tree','Tree'),
        ('flowers', 'Flowers'),
    ]

    SIZE_CHOICES =[
        ('L', 'Big'),
        ('M', 'Medium'),
        ('S', 'Small'),
    ]

    STATUS_CHOICES = [
        ('AVL', 'Available'),
        ('OOPS', 'Out of Stock')
    ]
    author = models.OneToOneField(Customer, on_delete=models.PROTECT, to_field='fullname', related_name="author_fullname")  # related to Customers Model
    title = models.CharField('Title', max_length=100, null=True)
    description = models.TextField('Image Description', max_length=200, null=True, blank=True)
    type = models.CharField('Type', max_length=10, choices=TYPE_CHOICES)
    theme = models.CharField('Theme', max_length=20, choices=THEME_CHOICES)
    size = models.CharField('Resolution', max_length=10, choices=SIZE_CHOICES)
    item_url = models.URLField('URL', max_length=250, unique=True)
    status = models.CharField('Status', max_length=30, choices=STATUS_CHOICES)



class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('PEN', 'Pending'),
        ('SHIP', 'Shipped'),
        ('DEL', 'Delivered')
    ]
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name="order_data")    # related to Customers Model
    order_date = models.DateTimeField('Date of Order', auto_now=True)
    order_status = models.CharField('Order Status', max_length=30, choices=ORDER_STATUS_CHOICES)
    # instead of price, barter_exchange field will define checkout response
    barter_exchange = models.BooleanField('Photo Exchanged ?', default=False, help_text="Clarifies if customer exchanged photos or not")

    def __str__(self):
        return f"Customer ID {self.customer_id}\nOrdered on {self.order_date}\nOrder Status : {self.order_status}"
    


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name="customer_data")    # related to Order Model
    product = models.ManyToManyField(Product, blank=True, related_name="product_status")      # related to Products Model
    quantity = models.IntegerField()

    def save_quantity(self, *args, **kwargs):
        self.quantity = len(self.product.id)
        super().save_quantity(*args, **kwargs)