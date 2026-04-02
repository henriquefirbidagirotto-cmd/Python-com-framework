# 1. Verificação de maioridade e permissão
# Enunciado:
# Crie um programa que leia a idade do usuário e se ele possui autorização dos pais (responda True ou False).
# O usuário pode participar da atividade se tiver 18 anos ou mais ou tiver autorização dos pais.
# Use and / or para verificar e exiba "Pode participar" ou "Não pode participar".

idade  = int(input('Idade: '))
autorizacao = input('Possui autorização?>>>  ')


pode  =  idade >= 18 and autorizacao == 'Pode'


msg =  pode and "pode" or "não pode"


print(msg)



# 2. Classificação de peso ideal
# Enunciado:
# Leia o peso (kg) e a altura (m) de uma pessoa. Calcule o IMC (peso / altura**2).
# Uma pessoa está com peso normal se o IMC estiver entre 18.5 e 24.9 (inclusive).
# Use operadores lógicos para verificar se o IMC está nessa faixa e exiba "Peso normal" ou "Fora da faixa".

peso = float(input('Peso:'))
altura = float(input('Altura:'))
imc = peso / altura ** 2
print(imc)
saude = imc > 18.5 and imc < 24.9
exibicao = saude and print('Pessoa saudavel')

# 3. Acesso ao sistema
# Enunciado:
# Leia o nome de usuário e a senha. O acesso é permitido apenas se o usuário for "admin" e a senha for "1234".
# Use and para verificar as duas condições e exiba "Acesso liberado" ou "Acesso negado".

usuario = str(input('Usuario:'))
senha = str(input('Senha:'))

verificacao_usu = usuario == 'admin' and senha == '1234'
entrar = verificacao_usu == True and print('você entrou')
erro = verificacao_usu == False and print('Usuario ou senha incorreto')

# 4. Compra com desconto
# Enunciado:
# Leia o valor da compra e se o cliente é VIP (True ou False).
# O cliente ganha 10% de desconto se o valor for maior que R$ 100 ou ele for VIP.
# Exiba o valor final com desconto (se aplicável) ou o valor original.

produto = float(input('Valor do Produto:'))
vip = str(input('Vip?'))
desconto1 = produto >= 100.0 or vip == 'Sim'
conta = produto * 0.9
valor = desconto1 == True and print('valor',conta)
valor2 = desconto1 == False and print('valor',produto)

# 5. Elegibilidade para doação de sangue
# Enunciado:
# Leia a idade e o peso.
# Para doar sangue, a pessoa deve ter entre 16 e 69 anos (inclusive) e pesar pelo menos 50 kg.
# Use and para verificar ambos os critérios e informe se a pessoa pode doar.

idade1 = int(input('idade: '))
peso1 = float(input('Peso: '))

ver = idade1 >= 16 and idade1 <= 69
ver_pes = peso1 > 50 

ver_idade = ver == True and print('idade dentro das normas de doação')
ver_idad = ver != True and print('idade fora das normas de doação')
ver_peso = ver_pes == True and print('peso ok')
ver_peso1 = ver_pes != True and print('peso fora dos padroes')

doar = ver_idade == True and ver_peso == True and print('Pode doar')
doar1 = ver_idade != True and ver_peso != True and print('Pode doar')

# 6. Validação de horário de funcionamento
# Enunciado:
# Uma loja funciona de segunda a sexta, das 9h às 18h.
# Leia o dia da semana (1=segunda, 7=domingo) e a hora (0 a 23).
# Determine se a loja está aberta.
# Dica: use and para combinar dia útil com horário, e or se quiser tratar sábado/domingo como fechado.

print('''
    Dias da semana
      
    1 = segunda
    2 = terça
    3 = quarta
    4 = quinta
    5 = sexta
    6 = sabado
    7 = domingo

''')

dia = int(input('Digite o dia da semana:'))
horario = int(input('horario:'))

verificacao_dia = dia  >= 1 and dia <= 5
verificacao_hora = horario >=9 and horario <= 18
ver_dia = verificacao_dia == True and print('Loja em dia comercial')
ver_hora = verificacao_hora == True and print('Loja aberta em horario comercial')
vern = not verificacao_dia == True and print('Loja Fechada, fora do dia de funcionamento')
vern_hora = not verificacao_hora == True and print('Loja fechada, fora do horario comercial')

# 7. Aprovação em duas disciplinas
# Enunciado:
# Leia as notas de Matemática e Português.
# O aluno é aprovado se ambas as notas forem maiores ou iguais a 6.
# Use and para verificar e exiba "Aprovado" ou "Reprovado".

mat = float(input('Digite a nota do aluno:'))
port = float(input('Digite a nota do aluno:'))

ver = mat >= 6 and port >= 6
ver1 = ver == True and print('Aprovado')
ver_n = not ver == True and print('Reprovado')

# 8. Identificação de ano bissexto
# Enunciado:
# Um ano é bissexto se for divisível por 4, mas não por 100, a menos que também seja divisível por 400.
# Leia um ano e use and e or para determinar se ele é bissexto.
# Exiba "Ano bissexto" ou "Ano não bissexto".

ano = int(input('Ano:'))

ver = ano % 4 == 0 or ano % 100 == 0 or ano % 400 == 0
ver1 = ver == True and print('Ano bissexto')
ver_n = not ver == True and print('Ano não bissexto')

# 9. Faixa etária
# Enunciado:
# Leia a idade e classifique:

# "Criança" se idade < 12

# "Adolescente" se 12 ≤ idade ≤ 17

# "Adulto" se idade ≥ 18
# Use and e or para definir os intervalos e exiba a classificação.

idade = int(input('Idade:'))
ver_crianca = idade < 12 and print('Criança')
ver_Adolecente = idade > 12 and idade < 17 and print('Adolecente')
ver_adulto = idade > 18 and print('Adulto')

# 10. Sistema de alerta de temperatura e umidade
# Enunciado:
# Leia a temperatura (°C) e a umidade (%).
# Dispare um alerta se temperatura > 35 ou umidade > 70.
# Caso contrário, exiba "Condições normais".
# Use or para combinar as condições.

c = float(input('Qual a temperatura:'))
umi = int(input('Umidade:'))

alerta = c > 35 or umi > 70
normal = not alerta == True and print('condições normais') or print('Alerta!!!')