
#Entendendo o self em classes
#classe é um molde sem dados
#Instancia da classe, tem dados
#uma classe gera varias instancias
#instancias sao os objetos 
#self é a propria isntancia

class Carro:
    def __init__(self, nome): #self é uma convenção, poderia ser qualquer coisa
        self.nome = nome

    #Neste exemplo bla faz papel de self
    # def __init__(bla, nome): #self é uma convenção, poderia ser qualquer coisa
    #     bla.nome = nome


    def acelerar(self):
        print(f'{self.nome} está acelerando...')

fusca = Carro('Fusca')
fusca.acelerar()# aqui corretamente estou chamdno o self
#Carro.acelerar() #estou chamando o proprio molde da classe ou seja da erro
Carro.acelerar(fusca)#agora estou especificando a minha instancia (self), 
#mas lembre-se, não é uma pratica comum

# print(fusca.nome)
# fusca.acelerar()


celta = Carro('Celta')
# print(celta.nome)