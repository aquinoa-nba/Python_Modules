from django.shortcuts import render


def django_page(request):
    context = {
        'title': 'Ex01: Django, framework web.',
    }
    return render(request, 'ex01/django_page.html', context=context)


def display_page(request):
    context = {
        'title': 'Ex01: Display process of a static page.',
    }
    return render(request, 'ex01/display_page.html', context=context)


def templates_page(request):
    context = {
        'title': 'Ex01: Template engine.',
    }
    return render(request, 'ex01/templates_page.html', context=context)
