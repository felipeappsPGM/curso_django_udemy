
from django.test import TestCase

from recipes import models


class RecipeTestBase(TestCase):
    def setUp(self) -> None:
        
        
        return super().setUp()
    
    def make_category(self, name='Category'):
        return models.Category.objects.create(name=name)
    
    def make_author(self,
            first_name='user',
            last_name='name',
            username='username',
            password='123456',
            email='user@user.com'):
        ...
        return models.User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email        )
    def make_recipe(
        self, 
        author,
        category,
        title='Recipe-title',
        description='Recipe description',
        slug='recipe-slug',
        preparation_time=10,
        preparation_time_unit='seconds',
        servings=5,
        servings_unit='porções',
        preparation_steps='Recipe preparation steps',
        preparation_steps_is_html=False,
        is_published=True,
        cover="oi"     
                    
        ):
        
        return models.Recipe.objects.create(
            category=category,
            author=author,
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
            is_published=is_published,
            cover=cover
        )
    