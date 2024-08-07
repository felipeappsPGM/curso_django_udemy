
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
        
    def test_recipe_search_can_find_recipe_by_title(self):
        title1 = 'This is recipe one'
        title2 = 'This is recipe two'
        
        recipe1 = self.make_recipe(
            slug = 'one345435',
            title = title1,
            author= self.make_author(),
            category=self.make_category()
        )
        recipe2 = self.make_recipe(
            slug = 'two245435',
            title = title2,
            author= self.make_author(
                first_name='user22',
                last_name='name22',
                username='username22',
                password='12345622',
                email='user@user.com22'),
            category=self.make_category(
                
            )
        )

        search_url = reverse('recipes:search')
        response1= self.client.get(f'{search_url}?q={title1}')
        response2= self.client.get(f'{search_url}?q={title2}')
        response_both = self.client.get(f'{search_url}?q=this')
        
        self.assertIn(recipe1, response1.context['recipes'])
        self.assertNotIn(recipe2, response1.context['recipes'])
        self.assertIn(recipe2, response2.context['recipes'])
        self.assertIn(recipe1, response_both.context['recipes'])
        self.assertIn(recipe2, response_both.context['recipes'])
        self.assertNotIn(recipe1, response2.context['recipes'])
        
