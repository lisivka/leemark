from django.shortcuts import render, redirect
from .forms import PostForm, PostForm2
from .models import Product
from django.contrib.auth import logout
from django.core.paginator import Paginator

def index(request):
    data = dict()
    # data['user'] = 'temp_admin'  # Временный админ (до включения авторизации)
    data['title'] = 'Galery Artwork'
    all_post = Product.objects.all()
    data['posts'] = all_post
    paginator = Paginator(all_post, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data['page_obj'] = page_obj
    return render(request, 'goods/index.html', context=data)


def create(request):
    data = dict()
    data['title'] = 'Add Artwork'
    if request.method == 'GET': # заходим на страницу в первый раз - поля пустые
        # Блокировка доступа через адресную строку
        # =======================
        if request.user.username == 'admin' or request.user.username == 'admin1':
            data['form'] = PostForm()
            return render(request, 'goods/create.html', context=data)
        else:
            logout(request)  # Блокировка доступа через адресную строку
            return redirect('/accounts/sign_in')
        # =======================

    elif request.method == 'POST': # нажата кнопка отправить, мы перехватываем форму
        filled_form = PostForm(request.POST, request.FILES)
        filled_form.save()
        return redirect('/goods')


def details(request, post_id):
    data = dict()
    data['title'] = 'View artwork'
    data['post'] = Product.objects.get(id=post_id)
    return render(request, 'goods/details.html', context=data)


def edit(request, post_id):
    data = dict()
    data['title'] = 'Edit artwork'
    post = Product.objects.get(id=post_id)
    # del ... ?
    if request.method == 'GET':
        # Блокировка доступа через адресную строку
        # =======================
        if request.user.username == 'admin' or request.user.username == 'admin1':
            data['form'] = PostForm2(instance=post)
            data['post'] = post
            return render(request, 'goods/edit.html', context=data)
        else:
            logout(request)  # Блокировка доступа через адресную строку
            return redirect('/accounts/sign_in')


    elif request.method == 'POST':
        form2 = PostForm2(request.POST)
        # print('==', form2)
        if form2.is_valid():
            # post.photo = form2.cleaned_data['photo']
            post.name = form2.cleaned_data['name']
            post.description = form2.cleaned_data['description']
            post.genre = form2.cleaned_data['genre']
            post.media = form2.cleaned_data['media']
            post.status = form2.cleaned_data['status']
            post.weight = form2.cleaned_data['weight']
            post.height = form2.cleaned_data['height']
            post.buy_url = form2.cleaned_data['buy_url']
            post.save()
            # update ?
        return redirect('/goods/details/'+str(post.id))


def delete(request, post_id):
    data = dict()
    data['title'] = 'Delete artwork'
    post = Product.objects.get(id=post_id)
    if request.method == 'GET':
        # Блокировка доступа через адресную строку
        # =======================
        if request.user.username == 'admin' or request.user.username == 'admin1':
            data['post'] = post
            return render(request, 'goods/delete.html', context=data)
        else:
            logout(request)  # Блокировка доступа через адресную строку
            return redirect('/accounts/sign_in')
    elif request.method == 'POST':
        post.delete()
        return redirect('/goods')