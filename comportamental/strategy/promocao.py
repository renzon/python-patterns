# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from decimal import Decimal

todos_descontos = []


def promocao(promo):
    """ Registra chamável como promoção

    :param promo:
    :return:
    """
    todos_descontos.append(promo)
    return promo


def desconto_null_object(pedido):
    return pedido.subtotal()


@promocao
def desconto_item_repetido(pedido):
    """ Fornece 10% de desconto em cima de items com quantidade igual ou
        superior a 10
    """
    desconto = pedido.soma_dos_items_com_quantidade_maior_que(10)
    desconto = desconto * Decimal('0.10')
    return pedido.subtotal() - desconto


@promocao
def desconto_grande_pedido(pedido):
    """Desconto de 5% para pedido maiores que 10.000"""
    subtotal = pedido.subtotal()
    if subtotal < 10000:
        return subtotal
    return subtotal * Decimal('0.95')


def melhor_promocao(pedido):
    return min(desconto(pedido) for desconto in todos_descontos)
