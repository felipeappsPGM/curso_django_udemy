from django.shortcuts import render
from utils.recipes.factory import make_recipe
# Create your views here.
from django.http import HttpResponse
#HTTP request
def home(resquest):
    
    return render(
        resquest,
        'recipes/pages/home.html',
        context= {
            'title': 'Home | Recipes',
            'recipes': [make_recipe() for _ in range(10)]
        },
        ) 

def recipe(resquest, id):
    return render(
        resquest,
        'recipes/pages/recipe-view.html',
        context= {
            'title': 'Receita | Recipes',
            'recipe': make_recipe(),
            'is_detail_page': True,
        },
        )

