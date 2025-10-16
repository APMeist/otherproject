from django.shortcuts import render

# Create your views here.


# Тут я просто ссылки на urls выведу, точнее вьювы захуячу. Все для дома: А




# Глав.страница


def main_page(request):
    return render(request, 'mainsite/mainpage.html')

def about_page(request):
    return render(request, 'mainsite/about.html')

