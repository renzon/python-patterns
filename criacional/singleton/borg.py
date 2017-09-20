class Borg:
    _estado_compartilhado = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.__dict__ = cls._estado_compartilhado
        return obj

    def apaga(self):
        return 'Apagando dados do BD de prod'


class SubBorg(Borg):
    def apaga(self):
        return 'Não apagando nada'


if __name__ == '__main__':
    obj1 = Borg()
    obj2 = SubBorg()
    print(id(obj1))
    print(id(obj2))
    obj1.a = 'a'
    print(obj1.a)
    print(obj2.a)
    print(obj1.apaga())
    print(obj2.apaga())
    print(type(obj1))
    print(type(obj2))
    print(obj2.apaga)
