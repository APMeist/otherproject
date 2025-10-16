from django.forms import ModelForm
from models import portfolio

class StudentPortfolio(ModelForm):
    class Meta:
        model = portfolio
        fields = ['name','fileportfolio','description']

#пока хз зачем оно тут но Тоха сказал надо, я поверил :И