from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile(AbstractUser):
    USER_CHOICES = [
        ('Artist', 'Art'),
        ('Photographer', 'Photography'),
        ('Enthusiast', 'Curiosity')
    ]

    # AbstractUser model fields - username, first_name, last_name, email, username, password, is_staff, is_active, date_joined
    # define additional or custom fields
    customer_type = models.CharField('Interested in ?', max_length=20, choices=USER_CHOICES)
    bio = models.TextField('Bio', max_length=200, null=True, blank=True)

    def __str__(self):
        fname = f"{self.first_name}".capitalize() 
        lname = f"{self.last_name}".capitalize()
        return f"{fname} {lname}"   

