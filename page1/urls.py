from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login/', views.Login_request, name='login'),
    path('logout/', views.logout_request, name='logout')
]