from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request, 'recipes/home.html',{
        'name': 'FELIPE',
    })

def contato(request):
    return HttpResponse('contato')

def sobre(request):
    return HttpResponse('sobre')

