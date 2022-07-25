from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('store/', views.store, name="store"),
    path('salachat/', views.salachat, name="salachat"),
    path('aboutme/', views.aboutme, name="aboutme"),
    path('login/', views.login, name="login"),
    path('register/',views.register, name="register"),
    path('logout/',LogoutView.as_view (template_name="core/logout.html"), name="logout"),
]