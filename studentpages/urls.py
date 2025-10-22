from django.urls import path
from . import views

urlpatterns = [
    path('', views.studenthome_page, name='studenthome'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    
    path('portfolio/', views.portfolio_page, name='portfolio_page'),
    
    path('create-lesson/', views.create_lesson, name='create_lesson'),
    #task & task-answer urls 
    #   - Я надеюсь, мне кажется, что сверху писала ИИшка. : А
    path('create-task/', views.create_task, name='create_task'),
    path('create-task-answer/', views.create_task_answer, name='create_task_answer'),
    path('update-task-answer/<int:id>', views.update_task_answer, name='update_task_answer'),
]