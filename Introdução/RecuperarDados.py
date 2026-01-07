import os 
import json

from Salvardados import Pessoa, caminho_arquivo
#recuperar dados salvos em json

with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)
    
    
    for pessoa in dados:
         p = Pessoa(pessoa['nome'], pessoa['sobrenome'])
         print(f'Nome: {p.nome} {p.sobrenome}')