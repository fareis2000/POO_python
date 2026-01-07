import os
import json
#salvar classe em json

caminho_arquivo = 'c:\\Users\\farei\\OneDrive\\Documentos\\Fabio\\Fabio\\Estudos_Python\\POO\\Introdução\\'
caminho_arquivo += 'pessoa.json'

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    

p1 = Pessoa('Fabio', 'Reis')
p2 = Pessoa('Ana', 'Silva')
p3 = Pessoa('João', 'Oliveira')
bd = [vars(p1), vars(p2), vars(p3)]


with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=4)
print('Arquivo salvo em:', caminho_arquivo)