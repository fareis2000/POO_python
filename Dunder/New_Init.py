from hashlib import new
class A:
    def __new__(cls):
        print('Antes')
        instancia = super().__new__(cls)
        print("deposi")
        instancia.x = 123 
        return instancia

    def __init__(self):
        print('sou o init')

    def __repr__(self):
        return 'A()'
    

# a = A()
# print(a.x)
# a = object.__new__(A)
# a.__init__()