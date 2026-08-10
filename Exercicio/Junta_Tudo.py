"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca

Pessoa (ABC)
    Cliente
        Clente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""

class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int, conta):
        super().__init__(nome, idade)
        self.conta = conta

class Conta:
    def __init__(self, agencia: str, numero: str, saldo: float):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor: float):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self.saldo += valor
        print(f"Depósito de {valor} realizado. Novo saldo: {self.saldo}")

    def sacar(self, valor: float):
        raise NotImplementedError("O método sacar deve ser implementado nas subclasses.")

class ContaCorrente(Conta):
    def __init__(self, agencia: str, numero: str, saldo: float, limite: float):
        super().__init__(agencia, numero, saldo)
        self.limite = limite

    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self.saldo + self.limite:
            raise ValueError("Saldo insuficiente para o saque.")
        self.saldo -= valor
        print(f"Saque de {valor} realizado. Novo saldo: {self.saldo}")

class ContaPoupanca(Conta):
    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente para o saque.")
        self.saldo -= valor
        print(f"Saque de {valor} realizado. Novo saldo: {self.saldo}")

class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []

    def adicionar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)
        self.contas.append(cliente.conta)

    def autenticar(self, cliente: Cliente, conta: Conta):
        if cliente not in self.clientes:
            raise ValueError("Cliente não pertence a este banco.")
        if conta not in self.contas:
            raise ValueError("Conta não pertence a este banco.")
        if cliente.conta != conta:
            raise ValueError("A conta não pertence ao cliente.")
        print("Autenticação bem-sucedida.")