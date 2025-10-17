from django.forms import ModelForm
from models import portfolio, lesson, task, taskanswer

class StudentPortfolio(ModelForm):
    class Meta:
        model = portfolio
        fields = ['name','fileportfolio','description']

#пока хз зачем оно тут но Тоха сказал надо, я поверил :И
# Оно нам надо для загрузки портфолио в БД :А

# Создание урока - для админов возможно сделать отдельно модель в таблице тип просмотра
class LessonForm(ModelForm):
     class Meta:
        model = lesson
        fields = ['group', 'subject', 'teacher', 'name']
        
        
 # Додумай сам       
class TaskForm(ModelForm):
    class Meta:
        model = task
        fields = ['title', 'description', 'deadline', 'task']
        

class TaskAnswerForm(ModelForm):
    class Meta:
             model = taskanswer
             fields = ['answerer', 'task', 'filesanswer']
             
# по формам вроде все - вопрос теперь по рестрикшонам.