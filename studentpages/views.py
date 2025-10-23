from django.shortcuts import render, redirect
from django.contrib import messages
from studentpages.models.user import User
from .models import Daylist, Portfolio, Lesson, Task, Taskanswer, Student
from .forms import LessonForm, TaskAnswerForm, TaskForm, ChangeMarkForm
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required - Вот что от тебя требую.


def home_page(request):
    return render(request, 'studentpages/home.html')

def studenthome_page(request):
    return render(request, 'studentpages/studenthome.html')
# CRUD portfolio
def portfolio_list_view(request):
    author = Portfolio.objects.get(id=id).name
    description = Portfolio.objects.get().description
    context = {'author': author, 'description': description}
    return render(request, 'studentpages/portfoliopage.html', context)
def portfolio_page(request):
    author = Portfolio.objects.all()
    return render(request, 'studentpages/portfoliopage.html', {'author': author})

def daylist_page(request):
    daylist = Daylist.objects.all()
    return render(request, 'studentpages/lessonpage.html', {'daylist': daylist})


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('studenthome')

    if request.method == 'POST':
        uslog = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(uslog=uslog)
        except:
            messages.error(request, 'Пусто')

        user = authenticate(request, username=uslog, password=password)

        if user is not None:
            login(request, user)
            return redirect('studenthome')
        else:
            messages.error(request, 'Ничего нет')

    context = {'page': page}
    return render(request, 'studentpages/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('studenthome')


# CRUD lesson
def create_lesson(request):
    form = LessonForm()  
    if request.method == 'POST': 
            Lesson.objects.create(
            teacher=request.teacher,
            name=request.POST.get('name'),
            subject=request.POST.get('subject'),
            description=request.POST.get('description'),
        )
            context = {'form': form}
            return redirect('studentpages/lessons.html', context),
    else:
        return render(request, 'studentpages/studenthome.html',)

def lesson_list_view(request):
    lessons = Lesson.objects.all().order_by('datetime')
    context = {'lessons': lessons}
    return render(request, 'studentpages/lessonpage.html', context)


# CRUD task
def task_list_view(request):
    tasks = Task.objects.all().order_by('datetime')
    context = {'tasks': tasks}
    return  render(request, 'studentpages/task.html', context)
def create_task(request):
    form = TaskForm()  
    if request.method == 'POST': 
            Task.objects.create(
                title=request.POST.get('title'),
                description=request.POST.get('description'),
                task=request.POST.get('task'),
                deadline=request.POST.get('deadline'),
            )
            context = {'form': form}
            return redirect('task_page', context),
    else:
        return render(request, 'studentpages/studenthome.html',)



def create_task_answer(request):
    form = TaskAnswerForm()

    if request.method == 'POST':
        # Получаем ID студента и задания
        student_id = request.POST.get('answerer')
        task_id = request.POST.get('task')

        # Преобразуем их в объекты моделей
        student = Student.objects.get(id=student_id)
        task = Task.objects.get(id=task_id)

        # Создаём ответ
        Taskanswer.objects.create(
            answerer=student,
            task=task,
            filesanswer=request.FILES.get('filesanswer'),  # если это файл
        )

        return redirect('task_answer.html')

    context = {'form': form}
    return render(request, 'studentpages/task_answer_form.html', context)
# задание для наших маленьких людей.


# Логика изменения ответа - нужно дать 

def update_task_answer(request, pk):
    taskanswer = Taskanswer.objects.get(pk=pk)
    form = TaskAnswerForm(instance=taskanswer)
    if request.method == 'POST':
        Task.name = request.POST.get('title')
        Task.fileanswer = request.POST.get('fileanswer')
        form.save()
        return redirect('taskanswer')
    context = {'form': form}
    return render(request, 'studentpages/task_answer_form.html', context)

def change_mark(request, pk):
    taskanswer = Taskanswer.objects.get(pk=pk)
    form = ChangeMarkForm(instance=taskanswer)
    if request.method == 'POST':
        form = ChangeMarkForm(request.POST, instance=taskanswer)
        if form.is_valid():
            form.save()
            messages.success(request, 'оценка сохранена')
            return redirect('task')
        else:
            messages.error(request, 'Ошибка при сохранении оценки')
    context = {'form': form}
    return render(request, 'studentpages/change_mark.html', context)