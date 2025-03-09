import pytest

from praktikum.bun import Bun


@pytest.mark.parametrize('name, price', [('AbCd', 1.5)])
class TestBun:
    def test_bun_init(self, name, price):
        bun = Bun(name=name, price=price)
        assert bun.name == name and bun.price == price

    def test_bun_get_name(self, name, price):
        bun = Bun(name=name, price=price)
        assert bun.get_name() == name

    def test_bun_get_price(self, name, price):
        bun = Bun(name=name, price=price)
        assert bun.get_price() == price
