from decimal import Decimal

import pytest

from comportamental.strategy.pedido import Item, Pedido


def test_adicionar_item():
    mac = Item('Mac', Decimal('9.32'), 2)
    pedido = Pedido()
    pedido.adicionar(mac)
    assert 1 == len(pedido._itens)


@pytest.mark.parametrize(
    'itens,total',
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
def test_subtotal(itens, total):
    pedido = Pedido()
    pedido.adicionar(*itens)
    assert Decimal(total) == pedido.subtotal()
