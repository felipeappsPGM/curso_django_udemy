from django.contrib import admin

from .models import Category, Recipe


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Recipe) # melhor forma de registrar no admin do django, mais simples
class RecipeAdmin(admin.ModelAdmin):
    ...
admin.site.register(Category, CategoryAdmin) #forma longa de registrar no admin do django