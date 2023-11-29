from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage


def paginate(request, products_list, items_per_page):
    
    paginator = Paginator(products_list, items_per_page)
    current_page = request.GET.get('page')
    try:
        page_content = paginator.page(current_page)
    except PageNotAnInteger:
        page_content = paginator.page(1)
    except EmptyPage:
        page_content = paginator.page(paginator.num_pages)

    return page_content