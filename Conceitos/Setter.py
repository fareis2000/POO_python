class Caneta:
    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None
    
    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        print(f'Setando cor para {valor}')
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        print(f'Setando cor da tampa para {valor}')
        self._cor_tampa = valor


caneta = Caneta('Azul')
caneta.cor = 'Vermelha'
caneta.cor_tampa = 'Preta'
print(caneta.cor)
print(caneta.cor_tampa)
