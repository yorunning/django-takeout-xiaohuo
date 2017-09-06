# -*- coding: utf8 -*-
from django.shortcuts import render, get_object_or_404
from takeout.models import secondMenu, Food
from user.models import User
from comments.forms import CommentForm
from django.db.models import Q

def index(request):
    return render(request, 'takeout/index.html')

def menu(request, menu_name):
    menu = secondMenu.objects.get(name=menu_name)
    food_list = list(Food.objects.filter(menu__name=menu_name))[:9]
    return render(request, 'takeout/menu.html', {
        'menu': menu,
        'food_list': food_list,
        })

def food(request, food_name):
    food = Food.objects.get(name=food_name)
    form = CommentForm()
    comment_list = food.comment_set.all()
    comments = list(comment_list)
    # for comment in comment_list:
    #     username = str(User.objects.get(username=comment.user))
    #     comments.append(username)
    return render(request, 'takeout/food.html', {
        'food': food,
        'form': form,
        'comments': comments
        })

def search(request):
    q = request.GET.get('q')
    error_msg = ''
    if not q:
        error_msg = '请输入关键词，例如 麻婆豆腐'
        return render(request, 'takeout/search.html', {'error_msg': error_msg})
    
    food_list = Food.objects.filter(Q(name__icontains=q))
    error_msg = '暂无该商品' if not food_list else '搜索结果如下'
    return render(request, 'takeout/search.html', {
        'food_list': food_list,
        'error_msg': error_msg
        })

def more(request, menu_name):
    menu = secondMenu.objects.get(name=menu_name)
    food_list = list(Food.objects.filter(menu__name=menu_name))
    return render(request, 'takeout/more.html', {
        'menu': menu,
        'food_list': food_list
        })