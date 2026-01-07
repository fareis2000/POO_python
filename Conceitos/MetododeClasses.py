class Pessoa:
    ano = 2024  # Atributo de classe compartilhado por todas as instâncias

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    

    @classmethod
    def metodo_exemplo(cls):
        print('hey')

    @classmethod
    def criar_familia_reis(cls, nome):
        return cls(nome, 'Reis')
    
    @classmethod
    def criar_sem_nome(cls, sobrenome):
        return cls('Anonima', sobrenome)

print(Pessoa.ano)  # Acessando o atributo de classe diretamente pela classe

p1 = Pessoa('Fabio', 'Reis')
p2 = Pessoa.criar_familia_reis('Ana')
p3 = Pessoa.criar_sem_nome('Silva')
p1.metodo_exemplo()
Pessoa.metodo_exemplo()
print(p1.nome, p1.sobrenome)
print(p2.nome, p2.sobrenome)
print(p3.nome, p3.sobrenome)
print(p1.ano)  # Acessando o atributo de classe através de uma inst
