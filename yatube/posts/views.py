from re import template
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    template = 'posts/index.html'
    text = 'Это главная страница проекта Yatube'
    context = {'text': text}
    return render(request, template, context)

# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_posts(request, any_slug):
    template = 'posts/group_list.html'
    text = 'Здесь будет информация о группах проекта Yatube'
    context = {'text': text}
    return render(request, template, context)
