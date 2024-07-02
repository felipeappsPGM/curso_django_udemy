from django.core.exceptions import ValidationError
from parameterized import parameterized

from recipes.models import Recipe
from recipes.tests.test_recipe_base import RecipeTestBase


class RecipeModelTestCase(RecipeTestBase):
    ...
    def setUp(self) -> None:
        self.recipe = self.make_recipe(category=self.make_category(), author=self.make_author())
        return super().setUp()
    
    def make_recipe_not_default(self):
        
        recipe = Recipe(
            author= self.make_author(username='felipe user aaa'),
            category= self.make_category(name='felipe frito aaa'),
            title='Recipe-title',
            description='Recipe description',
            slug='recipe-slug-for-no-defaults',
            preparation_time=10,
            preparation_time_unit='seconds',
            servings=5,
            servings_unit='porções',
            preparation_steps='Recipe preparation steps',

        )
        recipe.full_clean()
        recipe.save()
        return recipe
    
    def test_recipe_title_raises_error_if_title_has_more_than_65_chars(self):
        recipe = self.recipe
        self.recipe.title = "um valor qualquer que ultrapasse os sessenta e cinco caracteres, tive que add mais strings"
        # ou posso fazer
        self.recipe.title = 'FELIPE' * 70
        with self.assertRaises(ValidationError):
            self.recipe.full_clean() # AQUI A VALIDAÇÃO OCORRE SE TEM MAIS DE 65 CARACTERES DO MODEL

    @parameterized.expand([
            ('title', 65),
            ('description', 165),
            ('preparation_time_unit', 65),
            ('servings_unit', 65)
            
        ])
    def test_recipe_fields_max_lenght(self, field, max_lenght):
        setattr(self.recipe, field, 'A' * (max_lenght + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()
            
    def test_recipe_preparation_steps_is_html_is_false_by_default(self):
        recipe = self.make_recipe_not_default()
        self.assertFalse(
            recipe.preparation_steps_is_html,
            msg='recipe preparation_steps_is_html is not false'
        )
        
        
    def test_recipe_is_published_is_false_by_default(self):
        recipe = self.make_recipe_not_default()
        self.assertFalse(
            recipe.is_published,
            msg='recipe is_published id not false'
        )
        
    def test_recipe_string_representation(self): 
        needed = 'Testing Represetation'   
        self.recipe.title = needed
        self.recipe.full_clean()
        self.recipe.save()
        self.assertEqual(str(self.recipe), needed,
                         msg=f'Recipe string representation must be recipe "{needed}" but "{str(self.recipe)}" was received')