from django.core.paginator import Paginator
from django.shortcuts import render
from goods.models import Product


def index(request):
    data = dict()
    all_post = Product.objects.all()
    data['posts'] = all_post
    paginator = Paginator(all_post, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data['page_obj'] = page_obj
    return render(request, 'home/index.html', context=data)
