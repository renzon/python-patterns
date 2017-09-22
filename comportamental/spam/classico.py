from abc import ABC, abstractmethod


class SpamAbstrata(ABC):
    def enviar_spam_para_todos_usuarios(self, msg):
        # Obter a lista contatos
        for nome, endereco in self.obter_contatos():
            # Para cada usuario, enviar uma msg pelo canal
            self.enviar_mensagem(nome, endereco, msg)

    @abstractmethod
    def obter_contatos(self):
        """Deve retornar uma lista onde cada elemento é uma tupla. O primeiro
        elemento da tupla é o nome do contato e o segundo o seu endereço no
        respectivo canal de envio de mensagem"""

    @abstractmethod
    def enviar_mensagem(self, nome, endereco, msg):
        """ Deve enviar mensagem para usuario

        :param nome: str com nome do usuário
        :param endereco: str com endereço do usuário no canal
        :param msg: str mensagem a ser enviada
        :return: booleano indicando se mensagem foi enviada ou não
        """


if __name__ == '__main__':
    class SpamParaConsole(SpamAbstrata):
        def obter_contatos(self):
            return [('Renzo', 'renzo@email.com'),
                    ('Matheus', 'matheus@email.com')]

        def enviar_mensagem(self, nome, endereco, msg):
            print(f'Msg para {nome} no endereco {endereco}: {msg}')


    spam_para_console = SpamParaConsole()

    spam_para_console.enviar_spam_para_todos_usuarios('Olá Template Method')
