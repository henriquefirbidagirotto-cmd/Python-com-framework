# Parte 1: Escolha do Destino
#
# Quantidade de p Peça ao usuário:
# Nome do destinoessoas

viagens = {
    "Paris": {
        "preco": 5000,
        "vagas": 5
    },
    "Nova York": {
        "preco": 4000,
        "vagas": 3
    },
    "Tokyo": {
        "preco": 6000,
        "vagas": 2
    }
}

descon = []

print('Sistemas de Agencia de viagens')

print(viagens)

destino = input('Nome do destino:')
qnt_pessoas = int(input('Quantidade de pessoas:'))


# Parte 2: Cálculo do Valor
# Calcule:
# Valor total da viagem (preço * pessoas)
print('Destino',destino)
print('quantidade de pessoas:', qnt_pessoas)
cal = (viagens[destino])

calculo2 = (viagens[destino]['preco'])

print(cal)

calculo = (calculo2 * qnt_pessoas)
print(calculo)

# Parte 3: Regras da Agência (SEM if, SEM loop)

# Aplique:
# Se pessoas > 3 → desconto de 10%
desconto_de_dez = calculo * 0.1 
desconto = qnt_pessoas > 3
desconto and print('valor com o desconto de 10%:', calculo - desconto_de_dez)
# Se valor total > 10000 → desconto extra de 5%
desconto_extra1 = calculo * 0.05
desconto_extra = calculo >= 10000
desconto_extra and print('valor com desconto extra de 5%:', calculo - desconto_extra1)
desconto_total_conta = calculo * 0.15
desconto_total3 = desconto_extra and print('valor com desconto:', calculo - desconto_extra1)
desconto_total2 = desconto and print('valor com desconto:', calculo - desconto_extra1)
desconto_total = desconto and desconto_extra and print('valor com todos os descontos:', calculo - desconto_total_conta)
# Se não houver vagas suficientes → taxa de 500 (overbooking)

vagas = (viagens[destino]['vagas'])
pessoas = qnt_pessoas > vagas


desconto = qnt_pessoas > 3
p = (pessoas, ('overbooking'))
print(p)
taxa = pessoas and print('valor total por overbooking', desconto_total + 500)

# Se destino não existir → valor vira 0

inexistente = destino != 'Paris' or 'Tokyo' or 'Nova York'
existir = inexistente and print('Digite algo valido!!!')












