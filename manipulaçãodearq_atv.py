# Exercicicios de fixação 

# 1. **Criar e escrever**
    
#     Crie um programa que peça ao usuário um nome e uma idade, e grave essas informações em um arquivo chamado `cadastro.txt`,
# #  uma pessoa por linha no formato `"nome,idade"`. O programa deve permitir adicionar várias pessoas até que o usuário digite `"sair"`.
    
# def escrever_mostrar():
#     c = input('Deseja cadastra? sim ou sair')
#     while c == 'sim':
#         nome =  input('nome: ')
#         idade =  int(input('Idade:  '))
#         arquivo = open("cadastro.txt", "a")
#         arquivo.write(f"nome - {nome} idade - {idade}\n")
#         nome2 =  input('nome: ')
#         idade2 =  int(input('Idade:  '))
#         arquivo.write(f"nome - {nome2} idade - {idade2}\n")
#         c = input('Deseja cadastra? sim ou sair')

#     else:
#         arquivo.close()
#         print('Saiu...')
# escrever_mostrar()

# # 2. **Ler e exibir**
    
# #     Escreva um programa que leia o arquivo `cadastro.txt` criado no exercício anterior e exiba na tela cada pessoa no formato 
# # `"Nome: [nome], Idade: [idade]"`.

# with open("cadastro.txt", "r",encoding='utf-8') as arquivo:
#     nomes = arquivo.read()
#     print(nomes)

# # 3. **Contar linhas**
    
# #     Crie uma função `contar_linhas(nome_arquivo)` que retorna o número de linhas do arquivo. Teste com o arquivo `cadastro.txt`.
    
# def contar_linhas():
#     with open('cadastro.txt', 'r',encoding='utf-8') as arquivo:
#         linhas = arquivo.readlines()
#         print(len(linhas))

# contar_linhas()

# 4. **Procurar palavra**
    
#     Peça ao usuário uma palavra e um nome de arquivo. Conte quantas vezes essa palavra aparece no arquivo 
# (ignorando maiúsculas/minúsculas). Exiba o resultado.
    
# def procurar():
#     palavra = input('Palavra: ')
#     arq = input('Nome do arquivo: ')
#     try:
#         with open('cadastro.txt', 'r',encoding='utf-8') as arquivo:
#             cont = arquivo.read().lower()
#             qtd = cont.count(palavra)
#             print('A palavra ', palavra, ' aparece', qtd, 'vezes no arquivo.')
#     except:
#         print('Erro, Tente novamente')
# procurar()

# 5. **Copiar arquivo**
    
#     Peça ao usuário o nome de um arquivo de origem e um arquivo de destino.
#  Copie o conteúdo do arquivo de origem para o destino, mantendo as linhas.

def leitura(o, d):
    
   
    
    origem = open(o, 'w')
    origem.write('teste 1\n')
    origem.write('teste 2\n')
    origem.close()
    
    with open(o, 'r') as c :
        conteudo = c.read() 


        
        destino = open(d, 'w')
        destino.write(conteudo)
        destino.close()
  
    
    
     


o = input('Origem:')
d = input('destino:')


leitura(o,d)