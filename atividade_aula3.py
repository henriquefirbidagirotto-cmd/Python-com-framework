# Parte 1: Escolha do Destino
#
# Quantidade de p Peça ao usuário:
# Nome do destinoessoas


# Parte 2: Cálculo do Valor
# Calcule:
# Valor total da viagem (preço * pessoas)


# Parte 3: Regras da Agência (SEM if, SEM loop)

# Aplique:
# Se pessoas > 3 → desconto de 10%
# Se valor total > 10000 → desconto extra de 5%
# Se não houver vagas suficientes → taxa de 500 (overbooking)
# Se destino não existir → valor vira 0
print('Sistemas de Agencia de viagens')

destino = input('Nome do destino:')
qnt_pessoas = int(input('Quantidade de pessoas:'))

print(destino)
print(qnt_pessoas)

print(viagens[destino])
calculo = [viagens[destino * qnt_pessoas]]

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


