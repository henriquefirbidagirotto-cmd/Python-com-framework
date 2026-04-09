# ## **2  - Exercícios**

# ### **1. Tabuada Personalizada**

# Peça ao usuário um número inteiro positivo. Use `for` para exibir a tabuada desse número de 1 a 10.

# Validação para número positivo

# num = int(input('Digite um numero positivo: '))

# if num >= 0:
    
#     for i in range(1,11):

#         resul = num * i
#         print(num,'x',i,'=',resul)

# else:
#     print('Erro, digite um numero inteiro positivo')

# **Exemplo:**

# `Digite um número: 7` → exibe 7 x 1 = 7, 7 x 2 = 14, ..., 7 x 10 = 70.

# ---

# ### **2. Contagem Regressiva com Pausa**

# Peça um número inteiro positivo. Use `while` para fazer uma contagem regressiva até 0, exibindo cada número. Após o término, exiba `"Fogo!"`.

# num = int(input('Digite um numero inteiro positivo: '))
# c = num
# while c >= 1:
#     print('contagem regreciva', c)
#     c = c - 1

# ---

# ### **3. Média de Notas com `while`**

# Peça notas até que o usuário digite `-1`. Calcule e exiba a média das notas válidas (0 a 10). Ignore entradas inválidas e use `continue` quando necessário.

# c = 0
# lists = []

# print('Digite a nota ou -1 para sair')
# while c != -1:
#     nota = int(input('Digite a nota>'))
#     if nota == -1:

#         s = sum(lists)
#         saa = len(lists)
#         media = s / saa
#         print(media)
#         break


        

#     else:
#         lists.append(nota)
        
# s = sum(lists)
# saa = len(lists)
# media = s / saa


# ---

# ### **4. Validação de Senha com Limite de Tentativas**

# Defina uma senha fixa (ex: `"python123"`). Dê ao usuário 3 tentativas usando `while`. Se acertar, exiba `"Acesso liberado"` e encerre. Se errar todas, exiba `"Conta bloqueada"`.



tentativa = 3
while tentativa > 0:
    senha = input('Senha: ')
    tentativa = tentativa - 1
    if senha == 'python123':
        print('acesso liberado')
        break
        
        
    else:
        print('senha incorreta')
        print('tentativa', tentativa)

        



# ---

# ### **5. Números Primos**

# Peça um número inteiro positivo e determine se ele é primo. Use `for` com `range` e `break` para otimizar.

# ---

# ### **6. Sequência de Fibonacci**

# Gere os primeiros N termos da sequência de Fibonacci, onde N é informado pelo usuário. Use `for` ou `while` para iterar.

# ---

# ### **7. Soma de Dígitos**

# Peça um número inteiro positivo e calcule a soma de seus dígitos. Use `while` para extrair os dígitos um a um.

# ---

# ### **8 Menu Interativo**

# Crie um menu que permaneça ativo até que o usuário escolha a opção `"Sair"`. As opções podem ser:

# - `1` – Exibir mensagem "Olá!"
# - `2` – Exibir a data/hora atual (use `import datetime`)
# - `3` – Sair

# Use `while True` e `break` para sair.

# ---

# ### **9 Simulador de Lançamento de Dados**

# Simule 100 lançamentos de um dado de 6 faces. Conte quantas vezes cada face foi sorteada e exiba o resultado. Use `for` e `random.randint(1,6)`. (Importe `random`.)