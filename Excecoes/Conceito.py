# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)
class MeuError(Exception):
    ...
class OutroError(Exception):
    ...

def levantar():
    exception_ = MeuError('a', 'b', 'c')
    exception_.add_note('Essa é uma nota para a exceção')
    raise exception_

try:
    levantar()
except (MeuError, OutroError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = OutroError('lançando outro erro')
    exception_.__notes = error.__notes__.copy()
    exception_.add_note('Notas da exceção lançada')
    raise exception_ from error# relançando a exceção, mantendo o rastreamento da pilha de chamadas (stack trace)

