from django.urls import path
from . import views

#для студентов отдельные urls будут наверное :И

urlpatterns = [
    path('', views.portfolio_page, name='portfolio_page'),
    #пока указал портфолио как корень ветки /student/ :И
    path('daylist/', views.daylist_page, name='daylist_page'),
    #с этим тоже пока тестово так :И
]