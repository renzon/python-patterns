from criacional.singleton import cliente
from criacional.singleton.modulo import UNICA_INSTANCIA

if __name__ == '__main__':
    print(id(UNICA_INSTANCIA))
    print(id(cliente.UNICA_INSTANCIA))
