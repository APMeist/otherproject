from django.shortcuts import render, redirect
from django.contrib import messages
from studentpages.models.user import User
from .models import Daylist, Portfolio, Lesson, Task, Taskanswer, Student
from .forms import LessonForm, TaskAnswerForm, TaskForm
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required - Вот что от тебя требую.


def studenthome_page(request):
    return render(request, 'studentpages/studenthome.html')

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('studenthome')

    if request.method == 'POST':
        uslog = request.POST.get('uslog').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(uslog=uslog)
        except:
            messages.error(request, 'Пусто')

        user = authenticate(request, uslog=uslog, password=password)

        if user is not None:
            login(request, user)
            return redirect('studenthome')
        else:
            messages.error(request, 'Ничего нет')

    context = {'page': page}
    return render(request, 'studentpages/home.html', context)

def logoutUser(request):
    logout(request)
    return redirect('studenthome')

def portfolio_page(request):
    author = Portfolio.objects.all()
    return render(request, 'studentpages/portfoliopage.html', {'author': author})

def daylist_page(request):
    daylist = Daylist.objects.all()
    return render(request, 'studentpages/lessonpage.html', {'daylist': daylist})

# Логин будет тут - ща похер на него

# Создание урока

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

# Посмотри, что может быть еще сверху добавить, используй все, что хочешь. Я под таблами. Еще буду сидеть после тебя.    

# Функция изменения урока - она может содержать в себе изменения. Нам надо посмотреть - какие изменения необходимо делать. А так - сделать колонку в БД как кабинет и все.
#def updateLesson(request, pk):
    #lesson = lesson.objects.get(id=pk)
    #form = LessonForm(instance=lesson)
    
    
    
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

# Создание задания, тут потом выведем рестрикшн только лишь для учителя


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

