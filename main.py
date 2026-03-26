# 4  tipos
# str      int             float    bool
# textos numeros inteiros reais lógicos
# 'texto',  10 ,  5.2 ,  True , False
# 'Bom dia', 2026,1.80, 1 , 0
# 'Seu nome:',1, 60.200, 
# 'R$'


# ESTRUTURAS DE DADOS ****


# espaços na memória ram da maquina
# variar
# variaveis são dados únicos
# interpertador 
# meio termo linguagem 
# força indentação = organização
# OUTPUT - SAIDA - print()
# nomear de forma semantica  -  boa pratica


# regras para criar variáveis:
# _ ou letra
# não pode começar por números 
# não pode carcateres especiais 
# pode utilizar números(só não pode começar)
# palavra composta snake_case


# linguagem alto nivel
# interpretada
# dinamica - variáveis


print('CADASTRO DE USUÁRIOS:')


nome = 'Lucas Lima'
idade  =  25
email_usuario = 'lucas@gmail.com'
peso = 80.50
altura =  1.90
endereco = 'Rua 10, Jd X'
graduacao = 'ADS'
casado = False 


# SAÍDA
print(nome)
print(idade)
print(email_usuario)
print(endereco)
print(graduacao)
print(peso)
print(altura)
print(casado)


# ENTRADA


nome_2 = input('digite seu nome: ')
print(nome_2)

print('IMC')


peso =  float(input('Digite seu peso: '))
altura  =  float(input('Digite sua altura: '))
imc  =  peso/altura**2
print('IMC', imc)

print('SINAIS DE CALCULO ARITMÉTICO')



print(10+200) # soma
print(10-200) # subtração
print(10*200) # multiplicalçi
print(10/200) # divisão
print('modulo', 10%200) #módulo
print(10**2) # potencia
print(10//200.0) # divisão c/ 2 barras


# variáveis -  estruturas de dados 
# funções  - print() input() float() int()
# sinais aritmétivos 



# sinais lógicos


print(10 == 200) # comparar
print(10 > 200) # verifa se 1º numero é maior
print(10<200) # verifa se 1º numero é menor
print(10>=200) # maior ou iguael
print(10<=200) # menor ou igual
print(10 != 2) # diferente