from django.forms import ModelForm
from .models import Portfolio, Lesson, Task, Taskanswer

class StudentPortfolio(ModelForm):
    class Meta:
        model = Portfolio
        fields = ['name','fileportfolio','description']


class LessonForm(ModelForm):
     class Meta:
        model = Lesson
        fields = ['group', 'subject', 'teacher', 'name']
        
        
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'task']
        

class TaskAnswerForm(ModelForm):
    class Meta:
             model = Taskanswer
             fields = ['answerer', 'task', 'filesanswer']


class ChangeMarkForm(ModelForm):
    class Meta:
        model = Taskanswer
        fields = ['mark']
