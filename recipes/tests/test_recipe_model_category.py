
from django.core.exceptions import ValidationError

from recipes.tests.test_recipe_base import RecipeTestBase


class RecipeModelTestCase(RecipeTestBase):
    ...
    def setUp(self) -> None:
        self.category = self.make_category(name="testing category")
        return super().setUp()
    
    def test_recipe_category_model_string_represetation(self):
        self.assertEqual(
            str(self.category),
            self.category.name
        )
        
    def test_recipe_category_model_name_lenght_is_65_chars(self):
        self.category.name = 'A' * 66
        
        with self.assertRaises(ValidationError):
            self.category.full_clean()
    
    