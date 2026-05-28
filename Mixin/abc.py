from abc import ABC, abstractmethod


class Log(ABC):
    @abstractmethod
    def _log(self, msg):
        ...    
    def log_error(self, msg):
        return self._log(f'ERROR: {msg}')
    def log_success(self, msg):
        return self._log(f'SUCCESS: {msg}')

class logprintMixin(Log):
    def _log(self, msg):
        print(f'Logando a mensagem: {msg} em um arquivo de log em {self.__class__.__name__}')

lp = logprintMixin()
lp.log_error('Teste')