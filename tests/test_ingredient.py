import pytest
from praktikum.burger import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


@pytest.mark.parametrize('i_type, i_name, i_price', [(INGREDIENT_TYPE_SAUCE, 'cvn', 1.5)])
class TestIngredient:
    def test_ingredient_init(self, i_type, i_name, i_price):
        ingredient = Ingredient(ingredient_type=i_type, name=i_name, price=i_price)
        assert ingredient.type == i_type and ingredient.name == i_name and ingredient.price == i_price

    def test_ingredient_get_price(self, i_type, i_name, i_price):
        ingredient = Ingredient(ingredient_type=i_type, name=i_name, price=i_price)
        assert ingredient.get_price() == i_price

    def test_ingredient_get_name(self, i_type, i_name, i_price):
        ingredient = Ingredient(ingredient_type=i_type, name=i_name, price=i_price)
        assert ingredient.get_name() == i_name

    def test_ingredient_get_type(self, i_type, i_name, i_price):
        ingredient = Ingredient(ingredient_type=i_type, name=i_name, price=i_price)
        assert ingredient.get_type() == i_type
