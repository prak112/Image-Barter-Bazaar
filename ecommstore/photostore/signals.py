# to trigger signal function upon UserProfile instance creation/modification
from django.db.models.signals import post_save
# to pass created/modified UserProfile instance
from django.dispatch import receiver 
from users.models import UserProfile
from photostore.models import Customer


# UserProfile instance passed to create/modify Customer instance
@receiver(post_save, sender=UserProfile)
def create_customer_profile(sender, instance, created, **kwargs):
    if created: # new Customer instance
        Customer.objects.create(user_info=instance)
    
    else:   # existing Customer instance
        customer = Customer.objects.get(user_info=instance)
        customer.full_name = f"{instance.first_name} {instance.last_name}".capitalize()
        customer.customer_type = instance.user_type
        customer.save()
