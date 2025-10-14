from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.mainPage, name="mainpage"),
    path('about/', views.aboutPage, name="aboutpage"),
    path('admin/', admin.site.urls),
]