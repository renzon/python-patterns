from decimal import Decimal

import pytest

from comportamental.strategy.pedido import Item, Pedido
from comportamental.strategy.promocao import desconto_item_repetido


def test_adicionar_item():
    mac = Item('Mac', Decimal('9.32'), 2)
    pedido = Pedido()
    pedido.adicionar(mac)
    assert 1 == len(pedido._itens)


@pytest.mark.parametrize(
    'itens,subtotal',
    [
        (
                [Item('Mac', Decimal('9.32'), 2)],
                '18.64'
        ),
        (
                [
                    Item('Mac', Decimal('9.32'), 2),
                    Item('Galaxy', Decimal('1.03'), 3)
                ],
                '21.73'
        ),
    ]

)
def test_subtotal(itens, subtotal):
    pedido = Pedido()
    pedido.adicionar(*itens)
    assert Decimal(subtotal) == pedido.subtotal()


@pytest.fixture
def pedido_item_repetido():
    pedido = Pedido()
    pedido.adicionar(Item('Mac', Decimal('100.00'), 10))
    return pedido


def test_total_sem_promocao(pedido_item_repetido: Pedido):
    assert Decimal('1000.00') == pedido_item_repetido.total()


def test_total_com_desconto_por_item_repetido(pedido_item_repetido: Pedido):
    assert Decimal('900.00') == pedido_item_repetido.total(
        desconto_item_repetido)
