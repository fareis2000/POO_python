class Carro:
    def __init__(self, nome_carro):
        self.nome = nome_carro
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
fusca.fabricante = volkswagen
seisv = Motor('6V')
fusca.motor = seisv

print( fusca.nome, fusca.motor.nome, fusca.fabricante.nome )

fiat_uno = Carro('fiat_uno')
fiat = Fabricante('fiat')
fiat_uno.fabricante = fiat
motor10 = Motor('1.0')
fiat_uno.motor = motor10

print( fiat_uno.nome, fiat_uno.motor.nome, fiat_uno.fabricante.nome )