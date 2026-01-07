class Caneta:
    def __init__(self, cor):
        self._cor = cor
    
    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        self._cor = valor



caneta = Caneta('Azul')
caneta.cor = 'Vermelha'
print(caneta.cor)
