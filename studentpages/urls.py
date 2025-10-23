from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.home_page, name='home'),
    path(r'studenthome/', views.studenthome_page, name='studenthome'),
    path(r'login/', views.loginPage, name="login"),
    path(r'logout/', views.logoutUser, name="logout"),
    
    path(r'portfolio/', views.portfolio_page, name='portfolio_page'),
    
    path(r'create-lesson/', views.create_lesson, name='create_lesson'),
    #task & task-answer urls 
    path(r'create-task/', views.create_task, name='create_task'),
    path(r'create-task-answer/', views.create_task_answer, name='create_task_answer'),
    path(r'update-task-answer/<int:id>', views.update_task_answer, name='update_task_answer'),
]

