class Multiplicador:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self._multiplicador
        return wrapper


@Multiplicador(2)
def soma(x, y):
    return x + y

doismaisdois = soma(2, 2)
print(doismaisdois)  