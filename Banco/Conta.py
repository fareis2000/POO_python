import abc

class Conta:
    def __init__(self, agencia, numero, saldo) -> None:
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor): ... 

    
    def depositar(self, valor):
        self.saldo += valor
        self.detalhes()

    def detalhes(self, msg=''):
        print(f"O seu saldo é: {self.saldo:.2f} {msg}")