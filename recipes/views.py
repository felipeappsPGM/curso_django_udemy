from django.shortcuts import render

from recipes.models import Recipe
from utils.recipes.factory import make_recipe

# Create your views here.

#HTTP request
def home(resquest):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id') #pegando todas as Recipes do banco de dados
    
    return render(
        resquest,
        'recipes/pages/home.html',
        context= {
            'title': 'Home | Recipes',
            'recipes': recipes
        },
        ) 

#HTTP request
def category(resquest, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published=True
        ).order_by('-id') #pegando todas as Recipes do banco de dados
    
    return render(
        resquest,
        'recipes/pages/category.html',
        context= {
            'title': 'Category | Recipes',
            'recipes': recipes
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

