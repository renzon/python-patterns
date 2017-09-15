from threading import Lock


class Singleton:
    _instance = None

    def __new__(class_, *args, **kwargs):
        with Lock():
            if class_._instance is None:
                class_._instance = super().__new__(class_)
        return class_._instance

    def apaga(self):
        return 'Apagando dados do BD de prod'


class SubSingleton(Singleton):
    def apaga(self):
        return 'Não apagando nada'


if __name__ == '__main__':
    obj2 = SubSingleton()
    obj1 = Singleton()
    print(id(obj1))
    print(id(obj2))
    print(obj1.apaga())
    print(type(obj2))
    print(type(obj1))
