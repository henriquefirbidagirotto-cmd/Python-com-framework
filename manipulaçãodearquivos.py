# Abre o arquivo para escrita (cria/substitui)
arquivo = open("dados.txt", "w")
arquivo.write("Linha 1\n")
arquivo.write("Linha 2\n")
arquivo.close()



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