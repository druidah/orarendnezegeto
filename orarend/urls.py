from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('linkek/', views.user_links, name='user_links'),
    path('regisztracio/', views.register, name='register'),
    path('bejelentkezes/', auth_views.LoginView.as_view(), name='login'),
    path('kijelentkezes/', auth_views.LogoutView.as_view(), name='logout'),
    path('orarend/<int:pk>/', views.ics_link_detail, name='ics_link_detail'),  # Események megjelenítése az ICS link alapján
    path('', views.index, name='index'),  
]
