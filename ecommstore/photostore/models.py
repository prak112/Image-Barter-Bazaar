from django.db import models

from users.models import UserProfile

# Create your models here.

class Customer(models.Model): 
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    fullname = models.CharField('Full Name', max_length=128)
    type = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='customers')

    def save_fullname(self, *args, **kwargs):
        self.username = f"{self.user.first_name} {self.user.last_name}"
        super().save_fullname(*args, **kwargs)



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
    author = models.CharField('Author (full name)', max_length=72)  # associate to UserProfile Model
    title = models.CharField('Title', max_length=100, null=True)
    description = models.TextField('Image Description', max_length=200, null=True, blank=True)
    type = models.CharField('Type', max_length=10, choices=TYPE_CHOICES)
    theme = models.CharField('Theme', max_length=20, choices=THEME_CHOICES)
    size = models.CharField('Resolution', max_length=10, choices=SIZE_CHOICES)
    item_url = models.URLField('URL', max_length=250, unique=True)
    status = models.CharField('Status', max_length=30, choices=STATUS_CHOICES)