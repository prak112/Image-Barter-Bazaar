from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile(AbstractUser):
    class UserType(models.TextChoices):
        ART = 'Designer', 'Artist'
        PHOTOGRAPHY = 'Shutterbug', 'Photographer'
        CURIOSITY = 'Aficionado', 'Enthusiast'

    # AbstractUser model fields - first_name, last_name, email, username, password, is_staff, is_active, date_joined
    # define additional or custom fields
    user_type = models.CharField('Profession/Hobby', max_length=20, choices=UserType.choices)
    bio = models.TextField('Bio', max_length=200, null=True, blank=True)

    def __str__(self):
        fname = f"{self.first_name}".capitalize() 
        lname = f"{self.last_name}".capitalize()
        return f"{fname} {lname}"   

