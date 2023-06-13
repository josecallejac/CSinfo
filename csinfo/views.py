from django.shortcuts import render

# Create your views here.


def major(request):    
    return render(request, 'pages/torneo.html' )