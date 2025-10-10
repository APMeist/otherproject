from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect 

# Create your views here.


# Тут я просто ссылки на urls выведу, точнее вьювы захуячу. Все для дома: А




# Глав.страница


def mainPage(request):
    return render(request, 'mainsite/mainpage.html')


def aboutPage(request):
    return render(request, 'mainsite/about.html')

