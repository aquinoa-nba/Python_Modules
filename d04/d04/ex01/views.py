from django.shortcuts import render


def django_page(request):
    return render(request, 'ex01/django_page.html')


def display_page(request):
    return render(request, 'ex01/display_page.html')


def templates_page(request):
    return render(request, 'ex01/templates_page.html')
