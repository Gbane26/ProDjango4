from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pages/resto/index.html', data, context=RequestContext(request))

def menu(request):
    return render(request, 'pages/resto/menu.html')

def special(request):
    return render(request, 'pages/resto/special_dishes.html', {'present': present})

def team(request):
    return render(request, 'pages/resto/team.html')