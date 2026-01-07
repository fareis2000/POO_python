class Foo:
    def __init__(self):
        self.public = 'Public Attribute'
        self._protected = 'Protected Attribute'
        self.__private = 'Private Attribute'
    
    def metodo_public(self):
        self._metodo_protected()
        self.__metodo_private()
        print(self.__private)
        return 'Public Method'

    def _metodo_protected(self):
        print('_metodo_protected')
        return 'Protected Method'
    
    def __metodo_private(self):
        print('__metodo_private')
        return 'Private Method'
    

    
f = Foo()
print(f.metodo_public())

# print(f.public)          # Acesso permitido
# print(f.metodo_public())  # Acesso permitido
# print(f._protected)      # Acesso possível, mas desencorajado
# print(f._metodo_protected())  # Acesso possível, mas desencorajado
# print(f.__private)     # Acesso negado, gera AttributeError