
from django.contrib import admin
from django.urls import path

from recipes.views import recipe, home

app_name = 'recipes'

urlpatterns = [
    
    path('', home),
    path('home/', home, name="home"),
    path('recipe/<int:id>/', recipe, name="recipe"),
]
