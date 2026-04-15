import random

# ### **1. Calculadora com Funções**

# Crie funções separadas para as quatro operações básicas (`somar`, `subtrair`, `multiplicar`, `dividir`). Em seguida,
#  escreva um programa que leia dois números e a operação desejada (como string) e chame a função correspondente.
#  A divisão deve tratar divisão por zero.

# def calculo():
#     op = str(input('Digite a operação'))
#     x = 10
#     y = 20
#     try:
#         if op == 'somar':
#             s = x + y
#             print('resultado: ',s)
#         elif op == 'subtrair:':
#             s = x - y
#             print('resultado: ',s)
#         elif op == 'multiplicar:':
#             s = x * y
#             print('resultado: ',s)
#         elif op == 'dividir':
#             s = y / x
#             print('resultado: ',s)
#         else:
#             print('operação não pode ser realizada')            
#     except:
#         print('erro, Digite algo valido!')
# calculo()

# ### **2. Validador de CPF (simplificado)**

# Crie uma função `validar_cpf(cpf)` que recebe uma string com 11 dígitos e retorna `True`
# se for válido (use o algoritmo básico de validação de CPF). 
# Em seguida, teste a função com alguns CPFs.

# ERRO, ARRUMAR!!!

# def validar_cpf():
#     try:
#         cpf = str(input('CPF: '))
#         lis = [cpf]
#         ler = len(lis)
#         if ler != 12:
#             print('CPF INVAlIDO!')
#         else:
#             print('CPF VALIDO!')
#     except:
#         return 'Erro'


# validar_cpf()

# https://dicasdeprogramacao.com.br/algoritmo-para-validar-cpf/

# ### **3. Gerador de Tabuada**

# Escreva uma função `tabuada(numero, inicio=1, fim=10)` que exibe a tabuada do `numero` no intervalo `[inicio, fim]`. 
# Se os argumentos `inicio` e `fim` não forem fornecidos, use 1 e 10.

# def tabuada():
#     print('INICIO')
    
#     try:
#         num = int(input('Digite o numero que deseja ter a tabuada'))
#         if num != 0:
#             s = num * 1
#             s2 = num * 2
#             s3 = num * 3
#             s4 = num * 4
#             s5 = num * 5
#             s6 = num * 6
#             s7 = num * 7
#             s8 = num * 8
#             s9 = num * 9
#             s10 = num * 10

#             print(s)
#             print(s2)
#             print(s3)
#             print(s4)
#             print(s5)
#             print(s6)
#             print(s7)
#             print(s8)
#             print(s9)
#             print(s10)


#             print('Fim')
#         else:
#             print('0 não da para fazer a tabuada')
#     except:
#         print('Erro, Tente novamente')
# tabuada()

# ### **4. Contador de Palavras**

# Crie uma função `contar_palavras(texto)` que retorna um dicionário com a contagem de cada palavra no texto
# (considere palavras separadas por espaços).
# O programa principal deve ler uma frase e exibir o resultado.

# ### **5. Ordenação Personalizada**

# Implemente uma função `ordenar_lista(lista, crescente=True)` que retorna uma nova lista ordenada.
# Se `crescente=True`, ordena em ordem crescente; caso contrário, decrescente.
# Não use `sorted()` ou `list.sort()` (implemente o algoritmo de ordenação de sua escolha, como bolha).

### **6. Jogo de Adivinhação**

# Crie uma função `jogar()` que sorteia um número entre 1 e 100 e dá dicas ("maior", "menor") até o usuário acertar.
# Use `random.randint()`. A função deve retornar o número de tentativas. No programa principal, 
# chame a função e exiba quantas tentativas foram necessárias.

# def jogar():
#     n_a = random.randint(1,10)
    
    
#     c = 0
#     while c <= 100: 
#         escolha  =  int(input('1 à  100 >>> '))
#         if escolha  == n_a:
#             print('acertou!')
#             c = c + 1
#             print('Tentativas - ', c )
#             break
#         elif escolha > n_a:
#             print('É menor...')
#             c = c + 1
#             print('Tentativas - ', c )
#         elif escolha < n_a:
#             print('É maior... ')        
#             c = c + 1
#             print('Tentativas - ', c )
#         else:
#             print('Digite algo válido...')    
# jogar()

# ### **7. Conversor de Bases**

# Escreva uma função `converter_base(numero, base_origem, base_destino)` que converte um número entre bases 2, 8, 10 e 16.
# A entrada `numero` é uma string. A função retorna a string convertida. 
# (Exemplo: `converter_base("1010", 2, 16)` → `"A"`). Use `int()` com base e depois formate.

# def converte_base(numero, base_origem, base_destino):
#     numero = int(base_origem)

#     if base_destino == 2:
#         dado1 = bin(numero)
#         print(dado1)
#     elif base_destino == 8:
#         dado2 =  oct(numero)
#         print(dado2)
#     elif base_destino == 10:
#         print(str(numero))
#     elif base_destino == 16:
#         dado3 =  hex(numero)
#         print(dado3)

# converte_base("1010", 2, 8)


# Conteúdo para auxiliar

# https://dev.to/udanielnogueira/valores-em-binario-octal-e-hexadecimal-em-python-pn7

# ### **8. Sistema de Caixa Eletrônico**

# Crie uma função `sacar(valor)` que retorna um dicionário com a quantidade de notas de 100, 50, 20, 10, 5 e 2 necessárias para o valor.
# O valor deve ser inteiro e positivo. Caso não seja possível (valor não múltiplo de 2), a função retorna `None`. No programa principal,
# chame a função e exiba o resultado.

# def sacar(valor):



#     l =  [100,50,20,10,5,2]
#     d  =  {}


    
#     if valor % 2 != 0 or valor <= 0:
#         return None
    
#     for x in l:
#         q  =  valor //  x
#         d[x] = q  
#         valor %= x
#     return d


# print(sacar(350))

# ### **9. Análise de Lista com Múltiplos Retornos**

# Escreva uma função `analisar_lista(lista)` que retorna quatro valores: o menor valor,
# o maior valor, a soma e a média. No programa principal, receba uma lista de números do usuário (terminada por -1)
# e exiba os resultados usando desempacotamento.



# def analisar_lista(lista):
    
#     # menor
#     menor  =  m;in(lista)
#     # maior
#     maior = max(lista)
#     # soma 
#     soma  =  sum(lista)
#     # media 
#     media  =  soma / len(lista)
    
#     l =  []


#     l.extend([menor, maior, soma, media])


#     a,b,c,d = l


#     print(a,b,c,d)
       


#     return [menor, maior, soma , media]


# analise  =  analisar_lista([1,2,3,20,3040,150,0,66,99,10])


# print(analise)

# ### **10. Função que Modifica Lista Global**

# Crie uma lista global `estoque = []`. Escreva funções:

# - `adicionar_produto(nome, quantidade)`: adiciona um dicionário `{"nome": nome, "quantidade": quantidade}` à lista global.
# - `remover_produto(nome)`: remove o produto com esse nome (se existir).
# - `listar_estoque()`: exibe todos os produtos.
    
#  Use a palavra-chave `global` para modificar a lista dentro das funções. O programa principal deve apresentar
#  um menu interativo para o usuário.

# def adicionar_produto(nome, quantidade):
#     global estoque 
#     estoque  =  [{nome:quantidade}]
#     return estoque 

# # print(adicionar_produto('x', 2))

# def remover_produto(i):
#     estoque.pop(i)
#     return estoque
   


# def listar_estoque():
#     return estoque

# def main():
#   adicionar_produto('x', '0')
#   while True:  
#     menu =  int(input('''

#                 1 - add
#                 2 - remover
#                 3 - listar            


#                 '''))

#     if menu == 1:
#        prod = input('Nome produto: ')
#        q  =  int(input('Quantidade: '))
#        print(adicionar_produto(prod, q))

#     elif menu == 2:
#         print(listar_estoque())
#         prod = int(input('Nome produto: '))
#         remover_produto(prod)
        
#     elif menu == 3:
#         print(listar_estoque())




# main()