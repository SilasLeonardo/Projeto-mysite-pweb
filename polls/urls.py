from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

from . import sobre

urlpatterns = [
    path('', sobre.index, name='index'),
]