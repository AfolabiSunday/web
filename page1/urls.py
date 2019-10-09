from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('account/', include('django.contrib.auth.urls')), # django inbuilt login
    path('register', views.register, name='register'),
    path('login/', views.Login_request, name='login'), #function based login
    path('logout/', views.logout_request, name='logout')
]