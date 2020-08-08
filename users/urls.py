from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('profile/<int:id>', views.profile, name='profile'),
]
