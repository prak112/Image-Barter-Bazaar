# to trigger signal function upon UserProfile instance modification
from django.db.models.signals import post_save
# to pass modified UserProfile instance
from django.dispatch import receiver 
from users.models import UserProfile
from photostore.models import Customer


@receiver(post_save, sender=UserProfile)
# modified UserProfile instance passed to modify Customer instance
def create_customer_profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user_info=instance)

