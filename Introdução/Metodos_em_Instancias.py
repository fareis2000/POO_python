#Hard coded é algo passado diretamente ao codigo

class Carro:
    def __init__(self, nome):
        self.nome = nome

        #self.nome = 'Fusca' # Hard Coded

    def acelerar(self):
        print(f'{self.nome} está acelerando...')

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()


celta = Carro('Celta')
print(celta.nome)