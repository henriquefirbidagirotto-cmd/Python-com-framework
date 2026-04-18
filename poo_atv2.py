# ### **1. Classe Livro**

# Crie uma classe `Livro` com:

# - Atributos: `titulo`, `autor`, `ano`, `disponivel` (booleano, padrão True)
# - Métodos:
#     - `emprestar()`: se disponível, marca como False e exibe `"Livro emprestado"`; senão, exibe `"Indisponível"`
#     - `devolver()`: marca como True e exibe `"Livro devolvido"`
#     - `info()`: mostra todas as informações do livro
        
#         Crie dois livros, faça empréstimos e devoluções.
        
# class Livro:
#     def __init__(self, titulo, autor, ano, disponivel:bool):
#         self.titulo = titulo
#         self.autor = autor
#         self.ano = ano
#         self.disponivel = disponivel

#     def emprestar(self):
#         if self.disponivel == True:
#             return 'Livro emprestado'
#         else:
#             return 'Indisponivel'
        
#     def devolver(self):
#         if self.disponivel == True:
#             return 'Livro devolvido'
#         else:
#             return 'Livro pendente'
        
#     def info(self):
#         return 'O livro As 48 Leis do Poder é um guia prático que analisa as dinâmicas do poder com base em exemplos históricos e narrativas ilustrativas. O autor, Robert Greene, destaca que o poder desempenha um papel onipresente nas relações humanas e defende a importância de compreendê-lo para navegar com sucesso na sociedade.'
    
# livro = Livro('48', 'Robert Greene', 2020, True)
# print(livro.emprestar())
# devolucao = str(input('Devolução: '))
# if devolucao == 'sim':
#     print(livro.devolver())

# print(livro.info())

# ---

# ### **2. Classe Funcionário**

# Crie uma classe `Funcionario` com:

# - Atributos: `nome`, `cargo`, `salario_base`
# - Métodos:
#     - `aumentar_salario(percentual)`: aumenta o salário com base no percentual
#     - `calcular_bonus()`: retorna 10% do salário base
#     - `exibir_dados()`: exibe todas as informações
        
#         Crie um funcionário, aumente o salário e mostre os dados atualizados.
        
# class Funcionário:
#     def __init__(self, nome, cargo, salario_base):
#         self.nome = nome
#         self.cargo = cargo
#         self.salario = salario_base
        
#     def aumentar_salario(self, percetual):
#         salariop = self.salario + (self.salario * percetual)
#         return salariop
    
#     def calcular_bonus(self):
#         return self.salario * 0.10
        
    
#     def exibir_dados(self, asd):
#         return (f'nome', self.nome, 'cargo', self.cargo, 'salário', asd)
    
# funcionario = Funcionário('Henrique', 'Gerente', 8000)


# print(funcionario.aumentar_salario(0.10))
# print(funcionario.calcular_bonus())
# s = funcionario.aumentar_salario(0.10)
# s1 = funcionario.calcular_bonus()
# print(funcionario.exibir_dados(s + s1))

# ---

# ### **3./ Classe Calculadora (estática)**

# Crie uma classe `Calculadora` que **não precisa de atributos**. Apenas métodos de classe (use `@classmethod` ou métodos estáticos) para:

# - `somar(a, b)`
# - `subtrair(a, b)`
# - `multiplicar(a, b)`
# - `dividir(a, b)`
    
#     Teste os métodos sem criar objetos (chamando diretamente pela classe).
    
# class calculadora:
#     def somar(a, b):
#         return a + b

#     def subtrair(a, b):
#         return a - b

#     def multiplicar(a, b):
#         return a * b
    
#     def dividir(a, b):
#         if b == 0:
#             return 'Erro, divisão com 0'
#         else:
#             return a / b

# valor_a = int(input('A --> '))
# valor_b = int(input('b --> '))

# print(calculadora.somar(valor_a, valor_b))
# print(calculadora.subtrair(valor_a, valor_b))
# print(calculadora.multiplicar(valor_a, valor_b))
# print(calculadora.dividir(valor_a, valor_b))

# # ---

# ### **4. Classe Carro com Controle de Velocidade**

# Crie uma classe `Carro` com:

# - Atributos: `marca`, `modelo`, `velocidade` (inicial 0)
# - Métodos:
#     - `acelerar(valor)`: aumenta a velocidade (não pode ultrapassar 200 km/h)
#     - `frear(valor)`: diminui a velocidade (não pode ficar negativa)
#     - `velocidade_atual()`: exibe a velocidade
        
#         Crie um carro, acelere e freie até parar.

# class carro:
#     def __init__(self, marca, modelo, velocidade):
#         self.marca = marca
#         self.modelo = modelo
#         self.velocidade = velocidade

#     def acelerar(self):
#         self.velocidade = self.velocidade * 1.10
#         if self.velocidade > 200:
#             return 'ultrapassou 200 não poderá fazer esse ecu'
#         else:
#             return 'ecu liberado'
        
#     def frear(self):
#         freio = self.velocidade - self.velocidade
#         return 'velocidade', freio
    
#     def velocidade_atual(self):
#         return self.velocidade
                
# car = carro('BMW', '320i', 130)
# print(carro.acelerar(car))
# print(carro.frear(car))
# print(carro.velocidade_atual(car))

# ---

# ### **5. Classe Agenda**

# Crie uma classe `Agenda` que armazena contatos. Cada contato é um objeto da classe `Contato` (crie-a separada), com `nome`, `telefone` e `email`. A classe `Agenda` deve ter:

# - Atributo: `contatos` (lista)
# - Métodos:
#     - `adicionar_contato(contato)`: adiciona à lista
#     - `listar_contatos()`: exibe todos os contatos
#     - `buscar_contato(nome)`: exibe os dados do contato (se existir)
        
#         Crie alguns contatos, adicione-os à agenda e faça buscas.

class contatos:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

class Agenda:
    def __init__(self, contatos):
        self.contatos = contatos

    def adicionar_contatos(self, contato):
        self.contatos.addend(contato)
    
    def listar_contatos(self):
        return contatos_agenda
    
    def buscar_contato(self):
        nome = input('Pesquisar: ')
        for c in self.contatos:
            if nome.lower() in c.nome.lower():
                print(c)

        
        

contato_yasmin = contatos('yasmin', '11 94012-3232', 'yasmin@gmail.com')
contato_henrique = contatos('henrique', '11 92334-1235', 'hg@gmail.com')

contatos_agenda = ([contato_yasmin, contato_henrique])
agenda = Agenda(contatos_agenda)
buscar = input('Buscar: ')
if buscar == 'sim':
    Agenda.buscar_contato()

print(Agenda.listar_contatos())
print(Agenda.adicionar_contatos())
print(Agenda.buscar_contato())