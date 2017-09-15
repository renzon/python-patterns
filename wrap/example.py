class Engine:
    def start(self):
        return 'Start Engine'


class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        return self.engine.start()


if __name__ == '__main__':
    ferrari = Car()

    print(ferrari.start())
    print(ferrari.start)
