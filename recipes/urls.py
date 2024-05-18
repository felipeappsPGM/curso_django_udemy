

from django.urls import path

from recipes.views import category, home, recipe

app_name = 'recipes'

urlpatterns = [
    
    path('', home),
    path('home/', home, name="home"),
    path('recipe/category/<int:category_id>/', category, name='category'),
    path('recipe/<int:id>/', recipe, name="recipe"),
    
]
