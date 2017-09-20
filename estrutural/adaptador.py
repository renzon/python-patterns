class _Telefone:
    def telefonar(self, ddd, numero):
        print(f'ligando para ({ddd}) {numero}')


class _WhatsupApi:
    def call(self, phone):
        '''Phone must be on form +country code and phone number'''
        print(f'Zap Zap call to {phone}')


class WhatsupApiToTelefoneAdapter:
    def __init__(self, whats_api):
        self._whats_api = whats_api

    def telefonar(self, ddd, telefone):
        return self._whats_api.call(f'+55{ddd}{telefone}')


class _TelegramApi:
    def вызов(self, country_code, phone):
        print(f'Telegram phone call to {country_code} {phone}')


class TelegramParaTelefoneAdapterMixin:
    def telefonar(self, ddd, telefone):
        self.вызов('55', f'{ddd}{telefone}')


class TelegramParaTelefoneAdapter(TelegramParaTelefoneAdapterMixin,
                                  _TelegramApi):
    pass


telefone = TelegramParaTelefoneAdapter()

if __name__ == '__main__':
    # Imagine em mil lugares diferentes, em diferentes pacotes e modulos
    telefone.telefonar('12', '2345678')
    telefone.telefonar('12', '9876543')
