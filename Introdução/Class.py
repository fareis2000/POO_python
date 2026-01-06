# Classes são moldes para criar Objetos
# Classes geram novos objetos (Instancias)
# que podem ter seus proprios atributos e metodos
# Objetos podem ser mutaveis
# Por convenção usamos paschallcase para nomenclatura

# String = 'Luiz' # instancia de str
# print(String.upper())
# print(isinstance(String, str))

class Pessoa:
    #def se trata de um metodo dessa classe
    def __init__(self, nome, sobrenome):#Self sempre se tratara da nova instancia a ser criada
        self.nome = nome # atributo
        self.sobrenome = sobrenome # atributo

p1 = Pessoa("Fabio", "Reis")
# p1.nome = 'Fabio'
# p1.sobrenome = 'Reis'

print(p1)
print(p1.nome)
print(p1.sobrenome)