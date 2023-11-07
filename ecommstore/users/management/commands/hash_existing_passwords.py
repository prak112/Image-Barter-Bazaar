from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from users.models import UserProfile


class Command(BaseCommand):
    help = 'Hash existing user passwords'

    def handle(self, *args, **options):
        users = UserProfile.objects.all()
        for user in users:
            user.password = make_password(user.password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f"{user.username} - password hashed successfully!"))