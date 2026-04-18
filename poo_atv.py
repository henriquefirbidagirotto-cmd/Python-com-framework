# ### **1- Classe Pessoa**

# Crie uma classe `Pessoa` com os atributos `nome` e `idade`. Adicione um método `apresentar()
# ` que exiba `"Olá, meu nome é [nome] e -tenho [idade] anos.
# "` Crie duas pessoas diferentes e chame o método.

class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentação(self):
        print('meu nome é',self.nome, 'e tenho', self.idade, 'idade')

pessoa1 = pessoa('Henrique', 17)
pessoa1.apresentação()


# ---

# ### **2.Classe Retângulo**

# Crie uma classe `Retangulo` com os atributos `largura` e `altura`. Adicione métodos:

# - `calcular_area()` – retorna a área
# - `calcular_perimetro()` – retorna o perímetro
    
#     Crie um retângulo com largura 5 e altura 3 e exiba sua área e perímetro.
    
class retângulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.calcular_area = (self.largura * self.altura )
        self.calcular_perimetro = (self.largura *2)+(self.altura*2)

    def apresentar(self):
        print('A area do retangulo é', self.calcular_area, 'e o perimetro é', self.calcular_perimetro)

largura = int(input('Largura: '))
altura = int(input('Perimetro: '))

apresen = retângulo(largura, altura)
apresen.apresentar()
        

# ---

# ### **3.   Classe Conta Bancária**

# Crie uma classe `ContaBancaria` com:

# - Atributos: `titular`, `saldo` (inicial 0)
# - Métodos:
#     - `depositar(valor)`: acrescenta ao saldo
#     - `sacar(valor)`: se houver saldo suficiente, subtrai; senão, exibe `"Saldo insuficiente"`
#     - `exibir_saldo()`: mostra o saldo formatado
        
#         Crie uma conta, faça depósitos e saques e exiba o saldo.
        
class ContaBancária:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def visual(self):
        print('Conta bancaria: ')
        print('''
            1- depositar
            2- sacar
            3- exibir saldo
        ''')
        resp = int(input('--> '))
        if resp == 1:
            self.dep = float(input('Depositar: '))
            self.saldo = self.saldo + self.dep
            return 'saldo:', self.saldo
        elif resp == 2:
            self.saque = float(input('Saque: '))
            if self.saque <= self.saldo:
                self.saldo = self.saldo - self.saque
                return'saldo:', self.saldo
            else:
                return 'Saldo insuficiente'   
        elif resp == 3:
            return self.saldo
        else:
            print('Erro, tente novamnete')

saldo = ContaBancária('skibiridon', 0)
print(saldo.visual())

# ---

# ### **4. Classe Produto**

# Crie uma classe `Produto` com:

# - Atributos: `nome`, `preco`, `quantidade_estoque`
# - Métodos:
#     - `total_estoque()`: retorna `preco * quantidade_estoque`
#     - `adicionar_estoque(quantidade)`: aumenta a quantidade
#     - `remover_estoque(quantidade)`: diminui, mas não permite ficar negativo
        
#         Crie um produto, altere o estoque e exiba o valor total.
        
class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    def total_estoque(self):
        return self.preco * self.quantidade_estoque

    def adicionar_estoque(self, quantidade):
        self.quantidade_estoque += quantidade

    def remover_estoque(self, quantidade):
        if quantidade > self.quantidade_estoque:
            print("Erro: estoque insuficiente!")
        else:
            self.quantidade_estoque -= quantidade



prod1 = Produto("Chips", 12.99, 12)


prod1.adicionar_estoque(5)
prod1.remover_estoque(3)


print("Valor total em estoque:", prod1.total_estoque())


# ---

# ### **5. Classe Aluno**

# Crie uma classe `Aluno` com:

# - Atributos: `nome`, `matricula`, `notas` (lista de floats)
# - Métodos:
#     - `adicionar_nota(nota)`: adiciona à lista
#     - `calcular_media()`: retorna a média das notas
#     - `situacao()`: retorna `"Aprovado"` se média >= 7, `"Recuperação"` se >= 5, `"Reprovado"` caso contrário
        
#         Crie um aluno, adicione 3 notas e exiba sua situação.

class Aluno:
    def __init__(self, nome, matricula, notas):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)
    
    def situacao(self):
        media = self.calcular_media()
        if media >= 7:
            return 'Aprovado'
        elif media >= 5:
            return 'Recuperação'
        else:
            return 'Reprovado'


aluno = Aluno('Henrique', '22', [])

aluno.adicionar_nota(5.0)
aluno.adicionar_nota(7.0)
aluno.adicionar_nota(9.0)

print('Nome:', aluno.nome)
print('Média:', aluno.calcular_media())
print('Situação:', aluno.situacao())