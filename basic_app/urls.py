from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('special_page', views.special_page, name='special_page'),
    path('user_login', views.user_login, name='user_login')
]
