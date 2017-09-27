# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from abc import ABC, abstractmethod
from decimal import Decimal


class Desconto(ABC):
    """Classe base de todos descontos"""

    @abstractmethod
    def calcular_desconto(self, pedido):
        """Deve calcular o valor de desconto de acordo com o pedido."""


class _DescontoNullObjetc:
    def calcular_desconto(self, pedido):
        return pedido.subtotal()


desconto_null_object = _DescontoNullObjetc()


class _DescontoItemRepetido(Desconto):
    """ Fornece 10% de desconto em cima de items com quantidade igual ou
    superior a 10

    """

    def calcular_desconto(self, pedido):
        desconto = pedido.soma_dos_items_com_quantidade_maior_que(10)
        desconto = desconto * Decimal('0.10')
        return pedido.subtotal() - desconto


desconto_item_repetido = _DescontoItemRepetido()
