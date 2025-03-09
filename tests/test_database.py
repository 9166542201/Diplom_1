import pytest

from praktikum.database import Database
from unittest.mock import patch
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


@patch('praktikum.database.Ingredient')
@patch('praktikum.database.Bun')
@pytest.mark.parametrize('b_name, b_price', [('AbCd', 1.5)])
@pytest.mark.parametrize('i_type, i_name, i_price', [(INGREDIENT_TYPE_SAUCE, 'cvn', 1.5)])
class TestDatabase:

    def test_database_init(self, MockBun, MockIngredient, b_name, b_price, i_type, i_name, i_price):
        bun = MockBun()
        bun.configure_mock(name=b_name, price=b_price)

        ingredient = MockIngredient()
        ingredient.configure_mock(ingredient_type=i_type, name=i_name, price=i_price)

        database = Database()

        assert database.buns == [bun] * 3 and database.ingredients == [ingredient] * 6

    def test_database_available_buns(self, MockBun, MockIngredient, b_name, b_price, i_type, i_name, i_price):
        bun = MockBun()
        bun.configure_mock(name=b_name, price=b_price)

        ingredient = MockIngredient()
        ingredient.configure_mock(ingredient_type=i_type, name=i_name, price=i_price)

        database = Database()

        assert database.available_buns() == [bun] * 3

    def test_database_available_ingredients(self, MockBun, MockIngredient, b_name, b_price, i_type, i_name, i_price):
        bun = MockBun()
        bun.configure_mock(name=b_name, price=b_price)

        ingredient = MockIngredient()
        ingredient.configure_mock(ingredient_type=i_type, name=i_name, price=i_price)

        database = Database()

        assert database.available_ingredients() == [ingredient] * 6
