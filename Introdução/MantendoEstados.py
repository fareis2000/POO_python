class Camera:
    def __init__(self,nome,filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} Ja ta filmando....')
            return
        
        print(f'{self.nome} esta filmando...')
        self.filmando = True

    def Parar_filmar(self):
        if  not self.filmando:
            print(f'{self.nome} Nao ta filmando....')
            return
        
        print(f'{self.nome} esta parando de filmar...')
        self.filmando = False
    
    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} nao fotografa filamando irmao')
            return
        
        print(f'{self.nome} esta fotografando')

c1 = Camera('Canon')        
c2 = Camera('Sony')
c1.filmar()
c1.filmar()
c1.fotografar()
c1.Parar_filmar()
c1.fotografar()

print(c1.filmando)
print(c2.filmando)