from django.urls import path

from . import views

app_name = 'farmzoneweb'

urlpatterns = [
    path('', views.index, name='index'),
    path('/about', views.about, name='about'),
    path('/forum', views.forum, name='forum'),
    path('/market-place', views.marketplace, name='marketplace'),
    path('/contact', views.contact, name='contact'),
    path('/login', views.login, name='login'),
    path('/register', views.register, name='register'),
]
