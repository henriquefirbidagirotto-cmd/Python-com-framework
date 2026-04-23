# ### **Exercício 1 – Livro**

# Crie uma classe `Livro` com atributos de instância: `titulo`, `autor`, `ano`, `emprestado` (booleano, padrão `False`). Métodos:

# - `emprestar()` – se disponível, muda `emprestado` para `True`.
# - `devolver()` – muda `emprestado` para `False`.
# - `__str__()` – retorna uma string com as informações.
    
#     Teste com dois livros.
    

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.emprestado =  False
    def emprestar(self):
        if not self.emprestado:
            self.emprestado = True 


    def devolver(self):
        self.emprestado = False


    def __str__(self):
        return f'NOME: {self.titulo} AUTOR:{self.autor} ANO:{self.ano}'


# livro = Livro('antifragil', 'taleb', 2015)


# livro.emprestar()
# livro.devolver()


# print(livro) 


# ---

# ### **Exercício 2 – Contador com Atributo de Classe**

# Crie uma classe `Contador` que tenha um atributo de classe `total_contadores` que conta quantas instâncias foram criadas. Cada vez que um novo objeto é criado, 
# esse contador deve ser incrementado. Adicione um método `exibir_total()` que exibe o total de contadores criados.

# ---

class Contador:
    total_contadores = 0
    def __init__(self):
        Contador.total_contadores += 1
    @classmethod
    def exibir_total(self):
        print('Total no contador:', Contador.total_contadores)

# c1 = Contador()
# c2 = Contador()
# c3 = Contador()

# Contador.exibir_total()
    
# ### **Exercício 3 – Produto com Desconto**

# Classe `Produto` com atributos privados `_nome`, `_preco`, `_quantidade`. Use propriedades (`@property`) para acessar esses atributos.
#  Crie um método `aplicar_desconto(percentual)` que reduz o preço. O preço não pode ficar negativo. Teste criando produtos e aplicando descontos.

class Produto:
    def __init__(self, _nome, _preco, _quantidade):
        self._nome = _nome
        self._preco = _preco
        self._quantidade = _quantidade

    @property
    def nome(self):
        return self._nome
    
    @property
    def preco(self):
        return self._preco

    @property
    def quantidade(self):
        return self._quantidade

    def aplicar_desconto(self, percentual):
        desconto = self._preco * (percentual / 100)
        novo_preco = self._preco - desconto

        if novo_preco < 0:
            self._preco = 0

        else:
            self._preco = novo_preco

c = Produto('Ana', 100, 5)
c.aplicar_desconto(20)

# print(c.preco)

# ---

# ### **Exercício 4 – Banco com Saldo Privado**

# Classe `ContaBancaria` com atributo privado `__saldo`. Métodos:

# - `depositar(valor)` – aumenta saldo.
# - `sacar(valor)` – reduz saldo se houver saldo suficiente; senão, exibe mensagem.
# - `exibir_saldo()` – retorna o saldo (use propriedade `saldo` apenas para leitura).
    
#     Crie uma conta, realize operações e exiba o saldo.
    
class ContaBancaria:
    def __init__(self, __saldo):
        self.saldo = __saldo

    def depositar(self, valor):
        self.saldo = self.saldo + valor
        return self.saldo
    
    def sacar(self, valor):
        self.saldo = self.saldo - valor
        return 'saldo:',self.saldo, 'saque', valor
    
    def exibir_saldo(self):
        return self.saldo
    
c = ContaBancaria(1000)
c.depositar(100)
c.sacar(50)
#print(c.exibir_saldo())

# ---

# ### **Exercício 5 – Aluno com Notas**

# Classe `Aluno` com atributos: `nome`, `matricula` e uma lista privada `__notas`. Métodos:

# - `adicionar_nota(nota)` – adiciona à lista (valida de 0 a 10).
# - `calcular_media()` – retorna a média.
# - `situacao()` – retorna "Aprovado" se média >= 7, "Recuperação" se >= 5, "Reprovado" caso contrário.
    
#     Teste com um aluno e algumas notas.
    
class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.__notas = []  # lista privada

    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.__notas.append(nota)
        else:
            print("Nota inválida! Digite entre 0 e 10.")

    def calcular_media(self):
        if len(self.__notas) == 0:
            return 0
        return sum(self.__notas) / len(self.__notas)

    def situacao(self):
        media = self.calcular_media()

        if media >= 7:
            return "Aprovado"
        elif media >= 5:
            return "Recuperação"
        else:
            return "Reprovado"

    def __str__(self):
        return f"Aluno: {self.nome} | Média: {self.calcular_media():.2f} | Situação: {self.situacao()}"

aluno1 = Aluno('Mateus', 1222)

aluno1.adicionar_nota(5)
aluno1.adicionar_nota(6)
aluno1.adicionar_nota(8)

print(aluno1)


# ---

# ### **Exercício 6 – Data (validação)**

# Crie uma classe `Data` com atributos `dia`, `mes`, `ano`. No `__init__`, valide se a data é válida (considere meses com 30/31 dias e ano bissexto para fevereiro).
#  Use propriedades para garantir que alterações futuras também sejam validadas. Adicione um método `__str__` que retorna a data no formato `dd/mm/aaaa`.

# ---

# ### **Exercício 7 – Funcionário com Aumento**

# Classe `Funcionario` com atributos: `nome`, `cargo`, `salario_base` (privado). Métodos:

# - `aumentar_salario(percentual)` – aumenta o salário.
# - `calcular_bonus()` – retorna 10% do salário base.
# - Propriedade `salario` para leitura.
    
#     Teste criando um funcionário, aumente o salário e mostre o novo valor.
    

# ---

# ### **Exercício 8 – Carro com Velocidade (Encapsulamento)**

# Classe `Carro` com atributos `marca`, `modelo` e `__velocidade` (inicial 0). Métodos:

# - `acelerar(valor)` – aumenta velocidade até no máximo 200.
# - `frear(valor)` – reduz velocidade até no mínimo 0.
# - Propriedade `velocidade` para leitura.
    
#     Teste acelerando e freando.
    

# ---

# ### **Exercício 9 – Estatísticas (Atributos de Classe)**

# Classe `Estatistica` com atributos de classe `soma` e `contagem`. Métodos de classe:

# - `adicionar(valor)` – atualiza soma e contagem.
# - `calcular_media()` – retorna a média (ou 0 se nenhum valor adicionado).
    
#     Use `@classmethod` e não crie instâncias. Teste adicionando números e exibindo a média.
    

# ---

# ### **Exercício 10 – Agenda com Contatos (Composição)**

# Crie uma classe `Contato` com atributos `nome`, `telefone`, `email`. Crie uma classe `Agenda` que possui uma lista privada de contatos. Métodos:

# - `adicionar_contato(contato)` – adiciona à lista.
# - `listar_contatos()` – exibe todos os contatos.
# - `buscar_contato(nome)` – exibe os dados do primeiro contato com aquele nome.
    
#     Teste adicionando vários contatos e fazendo buscas.