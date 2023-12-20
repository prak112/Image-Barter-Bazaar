from django.contrib import admin

from users.models import UserProfile

# Register your models here.
@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display = ("__str__", "username", "email", "user_type", "date_joined", "last_login")
    list_display_links = ("username", )
    list_filter = ("user_type", )