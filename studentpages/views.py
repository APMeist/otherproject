from django.shortcuts import render
from .models import Portfolio
from .models import Daylist
# Create your views here.

def portfolio_page(request):
    author = Portfolio.objects.all()
    return render(request, 'studentpages/studenthome.html', {'author': author})
    #хз какой писать путь, пускай пока так
    #не знаю в каком формате тебе лучше, я подумал,
    # так то по сути через шаблонизатор jinja все можно вывести в нужном уже формате

def daylist_page(request):
    daylist = Daylist.objects.all()
    return render(request, 'studentpages/studenthome.html', {'daylist': daylist})