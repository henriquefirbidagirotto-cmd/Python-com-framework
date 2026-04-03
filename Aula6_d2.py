# Contexto
# Uma loja oferece um cupom especial. O cliente ganha o cupom se atender a pelo menos  das seguintes condições:
# Se for vip ou não(responde "sim" ou "não")
# Valor da compra acima de R$ 200
# Primeira compra no mês (responder "sim" ou "nao")
# Além disso, o cupom  pode ser aplicado se o cliente tiver  no histórico (número inteiro).Tarefa
# Receba:
# vip (string "sim" ou "nao")
# valor (float)
# primeira_compra (string "sim" ou "nao")
# itens_defeito (int)
# Determine se o cliente  ("Cupom liberado") ou  ("Sem cupom"),  (SEM IF , SEM LOOP, SEM FUNÇÃO)

valor_compra = float(input('Valor da compra: '))
vip = str(input('Possui VIP: '))
mes = str(input('primeira compra do mês: '))
His = str(input('Possui Historico de compra: '))

h = His == 'sim' or His == 's' and print('cupom pode ser aplicado')
ver = vip == 'sim' or vip == 's' or valor_compra > 200 or mes == 'sim' or mes == 's'
ver_n = not vip == 'sim' or not valor_compra > 200 or not mes == 'sim'
pri = ver == True and print('Cupom liberado')
pri1 = not ver == True and print('Sem cupom')

valor_compra2 = (valor_compra * 0.5)

conta = ver == True or h == True and print(valor_compra2) 

valor_final = pri == True and print(valor_compra * 0.5)

sem_cupom = not conta == True and print(valor_compra)

valorfin = pri == True or ver == True and print('valor:R$',valor_compra * 0.5)
valorfinsemcupom = not pri == True or not ver == True and print('valor:R$',valor_compra * 0.5)

recla = str(input('Possui alguma reclamação? '))