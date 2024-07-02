
from django.urls import resolve, reverse

from recipes.tests.test_recipe_base import RecipeTestBase
from recipes.views import recipe


class RecipeDetailViewTest(RecipeTestBase):

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1})) 
        self.assertIs(view.func, recipe)

        
    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertEqual(response.status_code, 404)
        
    


        
    def test_recipe_detail_template_loads_recipes(self):
        ...
        
        self.make_recipe(title='this is a detail page - It load one recipe',category=self.make_category(), author=self.make_author())
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        content = response.content.decode('utf-8')
        self.assertIn('porções', content)
        self.assertIn('this is a detail page - It load one recipe', content)
        self.assertIn('10 seconds', content)


    def test_recipe_detail_template_do_dont_load_recipe_not_published(self):
        """
        Test recipe is_published false dont show
        """
        ...
        recipe = self.make_recipe(is_published=False, category=self.make_category(), author=self.make_author())
        

        response = self.client.get(reverse('recipes:recipe', kwargs={'id': recipe.id}))
 
        self.assertEqual(response.status_code, 404)
        
        

