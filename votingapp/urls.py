from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vote/<uuid:choice_id>', views.vote, name='vote'),
]