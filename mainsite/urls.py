from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.main_page, name="mainpage"),
    path('about/', views.about_page, name="aboutpage"),
    path('student/', include('studentpages.urls')),
]