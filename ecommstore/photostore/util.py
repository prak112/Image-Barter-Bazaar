from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from urllib.parse import urlencode

from photostore.models import Product

def paginate(request, products_list, items_per_page):
    
    paginator = Paginator(products_list, items_per_page)
    current_page = request.GET.get('page')
    try:
        page_content = paginator.page(current_page)
    except PageNotAnInteger:
        page_content = paginator.page(1)
    except EmptyPage or InvalidPage:
        page_content = paginator.page(paginator.num_pages)
    except ValueError:
        # Modify URL to include filter conditions for filter_product
        filter_params = {
            'category': request.GET.get('category'),
            'theme': get_theme_code(request.GET.get('theme')),
            'author': request.GET.get('author'),
        }
        pagination_url = f"{request.path}?{urlencode(filter_params)}&page="
        page_content.paginator.base_url = pagination_url

    return page_content




def get_theme_code(theme_selected):
    theme_choices = Product.THEME_CHOICES
    selected_theme_code = ''
    for code, theme in theme_choices:
        if theme_selected == theme:
            selected_theme_code = code
    
    return selected_theme_code
    