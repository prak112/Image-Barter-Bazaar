from django.contrib.auth import get_user

def add_logout_status(request):
    user = get_user(request)
    logged_out = not user.is_authenticated

    return {
        'user_logged_out' : logged_out
    }