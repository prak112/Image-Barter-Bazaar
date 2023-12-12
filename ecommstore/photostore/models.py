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
    status = models.CharField('Status', max_length=30, choices=STATUS_CHOICES, default='AVL')

    def __str__(self):
        return f"\n{self.title}, authored by {self.author}\nTheme-{self.get_theme_display()}\n"



# staging items for purchase
class Cart(models.Model):
    customer_info = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, related_name="potential_customers")
    item = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name="products_in_cart")
    quantity = models.IntegerField(default=1, null=True)

    def save_quantity(self, *args, **kwargs):
        self.quantity = self.item.count()
        super().save_quantity(*args, **kwargs)

    def __str__(self):
        return f"\nCustomer-{self.customer_info.full_name}\nProducts in Cart-{self.item}\n"



# Customers' Order history
class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('SHIP', 'Shipped'),
        ('DEL', 'Delivered')
    ]
    customer_order = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, related_name="order_history")
    order_date = models.DateTimeField('Date of Order', auto_now=True)
    order_status = models.CharField('Order Status', max_length=30, choices=ORDER_STATUS_CHOICES)
    # instead of price, barter_exchange field will define checkout response
    payment = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name="images_exchanged")

    def __str__(self):
        return f"\n{self.customer_order.customer_info}\tOrder Status-{self.get_order_status_display()}\n"
