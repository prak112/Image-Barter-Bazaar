from django.db import models
from users.models import UserProfile


# Create your models here.
# Synchronized data with 'UserProfile'
class Customer(models.Model): 
    user_info = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="user_information")
    full_name = models.CharField('Full Name', max_length=128, unique=True)
    customer_type = models.CharField('Customer Type', max_length=20)

    # build fullname in UserProfile/utils.py
    def save(self, *args, **kwargs):
        fname = f"{self.user_info.first_name}".capitalize() 
        lname = f"{self.user_info.last_name}".capitalize()
        self.full_name = f"{fname} {lname}"   
        self.customer_type = self.user_info.user_type
        super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return f"\n{self.full_name}-{self.customer_type}\n"



# Details of Images hosted on 'photostore' app
class Product(models.Model): 
    CATEGORY_CHOICES = [
        ('PH', 'Photo'),
        ('ART', 'Art'),
    ]

    THEME_CHOICES = [
        ('MT', 'Mountain'),
        ('LK', 'Lake'),
        ('PLR', 'Polar'),
        ('FRST', 'Forest'),
        ('TR','Tree'),
        ('FLWR', 'Flowers'),
    ]

    STATUS_CHOICES = [
        ('AVL', 'Available'),
        ('OOPS', 'Out of Stock')
    ]
    
    author = models.CharField('Author', max_length=100, null=True)
    title = models.CharField('Title', max_length=100, null=True)
    description = models.TextField('Image Description', max_length=200, null=True, blank=True)
    image_url = models.URLField('Source', default='https://www.pexels.com/')
    category = models.CharField('Type', max_length=10, choices=CATEGORY_CHOICES)
    theme = models.CharField('Theme', max_length=20, choices=THEME_CHOICES)
    image = models.ImageField('Image', upload_to='images', default='images/flower-gold-mohar.jpg')
    status = models.CharField('Status', max_length=30, choices=STATUS_CHOICES)

    def __str__(self):
        return f"\n{self.title}, authored by {self.author}\tAvailability-{self.get_status_display()}\n"



# 
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
        return f"\n{self.customer.full_name}\tOrder Status-{self.order_status}\n"
    


# 
class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name="customer_data")    # related to Order Model
    product = models.ManyToManyField(Product, blank=True, related_name="product_status")      # related to Products Model
    quantity = models.IntegerField()

    def save_quantity(self, *args, **kwargs):
        self.quantity = len(self.product.id)
        super().save_quantity(*args, **kwargs)
    
    def __str__(self):
        return f"\nOrderID-{self.order.id}\n"