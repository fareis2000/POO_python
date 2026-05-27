#abstração

from pathlib import Path

log_file = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError('O método _log deve ser implementado pela subclasse')
    
    def log_error(self, msg):
        return self._log(f'ERROR: {msg}')
    def log_success(self, msg):
        return self._log(f'SUCCESS: {msg}')

class logfileMixin(Log):
    def _log(self, msg):
        msg_formatado = f'{msg}\n'
        print(f'salvando a mensagem: {msg} em um arquivo de log em {self.__class__.__name__}')
        with open(log_file, 'a') as arquivo:
            arquivo.write(msg_formatado)
            arquivo.write('-------------------\n')

class logprintMixin(Log):
    def _log(self, msg):
        print(f'Logando a mensagem: {msg} em um arquivo de log em {self.__class__.__name__}')


if __name__ == '__main__':
    lp = logprintMixin()
    lp.log_error('Teste')
    lp.log_success('Teste')
    lf = logfileMixin()
    lf.log_error('Teste')
    lf.log_success('Teste')
    print(log_file)