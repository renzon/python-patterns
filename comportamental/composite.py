from collections import namedtuple

Loja = namedtuple('Loja', 'perguntas')

loja1 = Loja(['Gosta de roupa'])
loja2 = Loja(['Gosta de fruta', 'Gosta de cerveja'])
lojas = [loja1, loja2]


class ExtratorDePerguntas:
    def __init__(self, loja):
        self._loja = loja

    def extrair(self):
        return self._loja.perguntas


class ExtratorDePerguntasMultiplas:
    def __init__(self, lojas):
        self._lojas = lojas

    def extrair(self):
        return list(self._extrair())

    def _extrair(self):
        for loja in self._lojas:
            yield from loja.perguntas


if __name__ == '__main__':
    dct_factory = {
        Loja: ExtratorDePerguntas,
        list: ExtratorDePerguntasMultiplas}
    escolhas = [loja1, lojas]
    for escolha in escolhas:
        cls = dct_factory[type(escolha)]
        print(cls)
        extrator = cls(escolha)
        print(extrator.extrair())
