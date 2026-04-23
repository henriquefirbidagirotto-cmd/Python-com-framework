class Dados:
    def __init__(self):
        self.nome = 'Ana' # publicp
        self._cpf = '123146' # protegido
        self.__conta = '1213' # privado


    def display(self):
        print(self.nome)
        print(self._cpf)
        print(self.__conta)


class Dados2(Dados):
    def __init__(self):
        super().__init__()
        self.x  =  10
        
    def mostrar(self):
        print(self._Dados__conta)



# d = Dados()
# d.display()
# print(d._Dados__conta)        
# print('cpf', d._cpf)


d2  =  Dados2()
d2.display()
d2.mostrar()