# Exercicicios de fixação 

# 1. **Criar e escrever**
    
#     Crie um programa que peça ao usuário um nome e uma idade, e grave essas informações em um arquivo chamado `cadastro.txt`,
#  uma pessoa por linha no formato `"nome,idade"`. O programa deve permitir adicionar várias pessoas até que o usuário digite `"sair"`.
    
def escrever_mostrar():
    c = input('Deseja cadastra? sim ou sair')
    while c == 'sim':
        nome =  input('nome: ')
        idade =  int(input('Idade:  '))
        arquivo = open("cadastro.txt", "a")
        arquivo.write(f"nome - {nome} idade - {idade}\n")
        nome2 =  input('nome: ')
        idade2 =  int(input('Idade:  '))
        arquivo.write(f"nome - {nome2} idade - {idade2}\n")
        c = input('Deseja cadastra? sim ou sair')
        
    else:
        arquivo.close()
        print('Saiu...')
escrever_mostrar()

# 2. **Ler e exibir**
    
#     Escreva um programa que leia o arquivo `cadastro.txt` criado no exercício anterior e exiba na tela cada pessoa no formato 
# `"Nome: [nome], Idade: [idade]"`.
    
def ler():
    c = input('deseja ver as informações do cadastro? ')
    while c == 'sim':
        ca = input('qual numero de cadastro? ')
        if ca == '1':
            arquivos = open('cadastro.txt', '')
            print('cadastro:',  )
ler()

# 3. **Contar linhas**
    
#     Crie uma função `contar_linhas(nome_arquivo)` que retorna o número de linhas do arquivo. Teste com o arquivo `cadastro.txt`.
    
# 4. **Procurar palavra**
    
#     Peça ao usuário uma palavra e um nome de arquivo. Conte quantas vezes essa palavra aparece no arquivo 
# (ignorando maiúsculas/minúsculas). Exiba o resultado.
    
# 5. **Copiar arquivo**
    
#     Peça ao usuário o nome de um arquivo de origem e um arquivo de destino.
#  Copie o conteúdo do arquivo de origem para o destino, mantendo as linhas.