from abc import ABC, abstractmethod



class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem
    
    @abstractmethod
    def enviar(self) -> bool:
        ...

class NotificacaoEmail(Notificacao):
        def enviar(self) -> bool:
            print(f'Enviando email com a mensagem: {self.mensagem}')
            return True

class NotificacaoSMS(Notificacao):
        def enviar(self) -> bool:
            print(f'Enviando SMS com a mensagem: {self.mensagem}')
            return True

def notificar(notificacao: Notificacao):
     notificacao_envada = notificacao.enviar()
     if notificacao_envada:
        print('Notificação enviada com sucesso!')
     else:
        print('Notificação não enviada.')

notificacaoemail = NotificacaoEmail('Olá, isso é um email!')
notificacaosms = NotificacaoSMS('Olá, isso é um SMS!')


notificar(notificacaoemail)
notificar(notificacaosms)