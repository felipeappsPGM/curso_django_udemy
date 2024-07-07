from unittest import skip

from django.urls import resolve, reverse

from recipes.tests.test_recipe_base import RecipeTestBase
from recipes.views import home


class RecipeHomeViewTest(RecipeTestBase):
 
   
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, home)

        
    def test_recipe_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)
        

        
    
        
    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get((reverse('recipes:home')))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')
    
    @skip('WIP') # isso faz pular essa função de teste  
    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h1>No recipes founds😪</h1>',
            response.content.decode('utf-8')
        )
        #Tenho que escrever mais algumas coisas sobre test
        self.fail('Para que eu termine de digitá-lo')
    def test_recipe_home_template_loads_recipes(self):
        ...
        
        self.make_recipe(category=self.make_category(), author=self.make_author())
        response = self.client.get(reverse('recipes:home'))
        context = response.content.decode('utf-8')
        self.assertIn('porções', context)
        self.assertIn('10 seconds', context)

        

        
    def test_recipe_home_template_do_dont_load_recipes_not_published(self):
        """
        Test recipe is_published false dont show
        """
        ...
        self.make_recipe(is_published=False, category=self.make_category(), author=self.make_author())
        

        response = self.client.get(reverse('recipes:home'))
 
        self.assertIn(
            '<h1>No recipes founds😪</h1>',
            response.content.decode('utf-8')            
        )
        

    def test_recipe_home_template_do_dont_load_recipes_not_published(self):
        """
        Test recipe is_published false dont show
        """
        ...
        self.make_recipe(is_published=False, category=self.make_category(), author=self.make_author())
        

        response = self.client.get(reverse('recipes:home'))
    
