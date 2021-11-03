from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_form, name='my_form'),
]
