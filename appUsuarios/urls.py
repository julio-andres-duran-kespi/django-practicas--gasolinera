
from django.urls import path
from . import views

app_name = 'appUsuarios'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('registro/', views.RegistroView.as_view(), name='registro'),
]

