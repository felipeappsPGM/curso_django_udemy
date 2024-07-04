
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render

from recipes.models import Recipe

# Create your views here.

#HTTP request
def home(request):
    # recipes = get_list_or_404(
    #     Recipe.objects.filter(
    #     is_published=True
    #     ).order_by('-id')
    # )
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    
    return render(
        request,
        'recipes/pages/home.html',
        context= {
            'title': 'Home | Recipes',
            'recipes': recipes
        },
        ) 

#HTTP request
def category(request, category_id):
    # recipes = Recipe.objects.filter(
    #     category__id=category_id,
    #     is_published=True
    #     ).order_by('-id') #pegando todas as Recipes do banco de dados
    
    # if not recipes:
    #     raise Http404('not found🤷‍♂️')
    
    recipes = get_list_or_404(Recipe.objects.filter(
        category__id=category_id,
        is_published=True,
        ).order_by('-id'))    
    return render(
        request,
        'recipes/pages/category.html',
        context= {
            'title': f'{recipes[0].category.name} - Category | Recipes',
            'recipes': recipes
        },
        ) 

def recipe(request, id):
    recipe = Recipe.objects.filter(
        pk=id,
        is_published=True,
    ).order_by('-id').first()
    recipe = get_object_or_404(Recipe, pk=id, is_published=True)
    return render(
        request,
        'recipes/pages/recipe-view.html',
        context= {
            'title': f'{recipe.title} | Recipes',
            'recipe': recipe,
            'is_detail_page': True,
            
        },
        )

def search(request):
    ...
    search_term = request.GET.get('q', '').strip()
    
    if not search_term:
        raise Http404()
    
    recipes = Recipe.objects.filter(
        Q(
            Q(title__icontains = search_term) | # utilizar __icontains para buscar termos dentro de title 
            Q(description__icontains = search_term),
        ),
        is_published=True,

    )
    
    recipes = recipes.order_by('-id')
    recipes = recipes.filter(is_published=True)
    
    return render(
        request,
        'recipes/pages/search.html',
       context= {
            'title': f'Search for {search_term} |',
            'search_term': search_term,
            'recipes': recipes
            
        },
    )
