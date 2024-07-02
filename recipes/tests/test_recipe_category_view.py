
from django.urls import resolve, reverse

from recipes.tests.test_recipe_base import RecipeTestBase
from recipes.views import category


class RecipeCategoryViewTest(RecipeTestBase):
 
   

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, category)
        

        
    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertEqual(response.status_code, 404)

    

    def test_recipe_category_template_loads_recipes(self):
        ...
        
        self.make_recipe(title='this is a category test',category=self.make_category(), author=self.make_author())
        response = self.client.get(reverse('recipes:category', args=(1,)))
        context = response.content.decode('utf-8')
        self.assertIn('porções', context)
        self.assertIn('this is a category test', context)
        self.assertIn('10 seconds', context)
        


        
    def test_recipe_category_template_do_dont_load_recipes_not_published(self):
        """
        Test recipe is_published false dont show
        """
        ...
        recipe = self.make_recipe(is_published=False, category=self.make_category(), author=self.make_author())
        

        response = self.client.get(reverse('recipes:recipe', kwargs={'id': recipe.category.id}))
 
        self.assertEqual(response.status_code, 404)


        

        
