# memo_app/urls.py
from django.urls import path
from . import views

app_name = 'memo_app'
urlpatterns = [
    path('', views.index, name='index'),
]