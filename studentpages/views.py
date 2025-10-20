
from django.shortcuts import render, redirect

from studentpages.models import task


from .models import Daylist, Portfolio, Lesson, Task, Taskanswer
from .forms import LessonForm, TaskAnswerForm, TaskForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def portfoliopage(request):
    author = Portfolio.objects.all()
    return render(request, 'studentpages/portfoliopage.html', {'author': author})

def daylist_page(request):
    daylist = Daylist.objects.all()
    return render(request, 'studentpages/lessonpage.html', {'daylist': daylist})

# Логин будет тут - ща похер на него

























# Создание урока

def createlesson(request):
    form = LessonForm()  
    if request.method == 'POST': 
            Lesson.objects.create(
            teacher=request.teacher,
            name=request.POST.get('name'),
            subject=request.POST.get('subject'),
            description=request.POST.get('description'),
        )
            return redirect('studentpages/lessons.html'),

# Посмотри, что может быть еще сверху добавить, используй все, что хочешь. Я под таблами. Еще буду сидеть после тебя.    

# Функция изменения урока - она может содержать в себе изменения. Нам надо посмотреть - какие изменения необходимо делать. А так - сделать колонку в БД как кабинет и все.
#def updateLesson(request, pk):
    #lesson = lesson.objects.get(id=pk)
    #form = LessonForm(instance=lesson)
    
    
    
def createTask(request):
    form = TaskForm()  
    if request.method == 'POST': 
            Task.objects.create(
                title=request.POST.get('title'),
                description=request.POST.get('description'),
                task=request.POST.get('task'),
                deadline=request.POST.get('deadline'),
            )
            return redirect('task_page'),

def updateTask(request, pk):
    form = TaskForm(instance=task)
# Создание задания, тут потом выведем рестрикшн только лишь для учителя


def createTaskAnswer(request):
    form = TaskAnswerForm
    if request.method == 'POST':
            Taskanswer.objects.create(
                answerer=request.POST.get('answerer'),
                task=request.POST.get('task'),
                filesanswer=request.POST.get('filesanswer'),
            )
            return redirect('task_answer_page'),
    context = {'form': form}  
    return render(request, 'studentpages/taskanswerform.html', context)
# задание для наших маленьких людей.


# Логика изменения ответа - нужно дать 

def updateTaskAnswer(request, pk):
    taskanswer = Taskanswer.objects.get(pk=pk)
    form = TaskAnswerForm(instance=taskanswer)
    if request.method == 'POST':
        Task.name = request.POST.get('title')
        Task.fileanswer = request.POST.get('fileanswer')
        form.save()
        return redirect('taskanswer')
    context = {'form': form}  
    return render(request, 'taskanswerform.html', context)   
    
# HTML будут новые - пока сделаны для тестирования тебе и понимания всего. 

# Я просто хочу тут написать - я ненавижу все, особенно, когда сидеть надо с 5 утра. Три энергетика и не один не заработал

