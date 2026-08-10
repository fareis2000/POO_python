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
        self.detalhes(f'(DEPOSITO {valor})')

    def detalhes(self, msg=''):
        print(f"O seu saldo é: {self.saldo:.2f} {msg}")
        print('__')

class poupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SACANDO {valor})')
            return self.saldo

        print('nAO DEU PARA SACAR IRMAO')
        self.detalhes(f'(SAQUE NEGADO {valor})')

class corrente(Conta):

    def __init__(self, agencia, numero, saldo, limite) -> None:
            super().__init__(agencia, numero, saldo)
            self.limite = limite

    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SACANDO {valor})')
            return self.saldo

        print('nAO DEU PARA SACAR IRMAO')
        self.detalhes(f'(SAQUE NEGADO {valor})')

if __name__ == "__main__":
    cp1 = poupanca(111, 222, 0)
    cp1.sacar(1)
    cp1.depositar(1)
    cp1.sacar(1)