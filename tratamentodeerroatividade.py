# 1
# # Trate o TypeError -  Qual expressão deve ser gerada para ele aparecer?

try:
    x = input('>>>')
    print(100 + x)

except TypeError:
    print('typeerror')

else:
    print('algo valido')

finally:
    print('carregando')

# 2
# # Trate o ValueError -  Crie em python o erro 

try:
    x = int(input('>>>'))
    print(90 + x)

except ValueError:
    print('dado incorreto de acordo com o input')

else:
    print('algo deu errado')

finally:
    print('codigo carregado')

# 3
# # Exercício: Dada uma lista, solicite ao usuário um índice e imprima o 
# # elemento correspondente,
# # lidando com exceções caso o índice fornecido esteja fora dos limites da lista.

try:
    x = int(input('Digite o dado que quer pegar da lista:'))
    list = [1,2,3,4,5,6,7]
    x1 = x - 1
    l = list[x1]
    print(l)

except IndexError:
    print('imcompativel com a lista')

finally:
    print('codigo carregado')

# 4
# # Peça ao usuário para inserir um número inteiro, tente convertê-lo 
# # para um número real,
# # lidando com exceções caso a entrada não seja um número ou não 
# # seja possível converter para real.

try:
    x = int(input('insira um numero:'))
    x1 = float(x)
    print(x1)

except TypeError:
    print('insira um numero inteiro')

except ValueError:
    print('numero impossivel de converter para real ')

finally:
    print('codigo carregado')

# 5
# # Exercício: Peça ao usuário para inserir dois números afaça a divisão do primeiro  
# # pelo segundo, lidando com exceções caso o segundo número 
# # seja zero.

try:
    x = int(input('digite um numero'))
    x1 = int(input('digite um numero'))

    x2 = x / x1 or x1 / x
    print(x2)

except ZeroDivisionError:
    print('0 nao e divisivel')

except ValueError:
    print('coloque um numero compativel com o input')

finally:
    print('codigo carregado')
