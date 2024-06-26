
from django.urls import resolve, reverse

from recipes.tests.test_recipe_base import RecipeTestBase
from recipes.views import search


class RecipeSearchViewTest(RecipeTestBase):     
        
    def test_recipe_search_uses_correct_view_functions(self):
        url = reverse('recipes:search')
        resolved = resolve(url)
        self.assertIs(resolved.func, search)

    def test_recipe_search_loads_correct_template(self):
        response = self.client.get(reverse('recipes:search') + '?q=teste')
        self.assertTemplateUsed(response, 'recipes/pages/search.html')
        
    def test_recipe_search_raises_404_if_no_search_term(self):
        url = reverse('recipes:search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        
        
    def test_recipe_search_term_is_on_page_title_and_escaped(self):
        url = reverse('recipes:search') + '?q=<Teste>'
        response = self.client.get(url)
        
        self.assertIn(
            'Search for &lt;Teste&gt;',
            response.content.decode('utf-8')
        )