from photostore.models import Product
from .global_context import global_context

def products_context(request):
    # access rand_photo, rand_art variables
    global_context_variables = global_context(request)
    random_photo = global_context_variables["random_photo"]
    random_art = global_context_variables["random_art"]

    # dropdown filter options
    categories = [category[1] for category in Product.CATEGORY_CHOICES]
    theme_names = [theme[1] for theme in Product.THEME_CHOICES]
    authors = Product.objects.values_list('author', flat=True).distinct()

    # Define the context variables
    context = {
        "random_photo": random_photo,
        "random_art": random_art,
        "categories" : categories,
        "themes" : theme_names,
        "authors" : authors,
            }

    # Return the context variables as a dictionary
    return context