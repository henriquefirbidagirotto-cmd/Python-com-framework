# Peça o valor de um produto e:

# Calcule um desconto de 10%.

# Mostre o valor final.

# Verifique se o valor final é maior que 100.

# Verifique se o produto ficou barato (menor que 50).

# meu jeito

print('compra com desconto')
print('digite o valor do produto!')
produto = float(input('valor:'))

desconto = (produto / 10)
desconto_final = (produto - desconto)
print('valor com desconto fica:',desconto_final)

if desconto_final >= 100:
    print('sua conta deu mais que 100')
    print('sua conta deu', desconto_final)
elif desconto_final <= 50:
    print('sua conta deu menos que 50')
    print('sua conta deu', desconto_final)
else:
    print('sua conta deu', desconto_final)
print('formas de pagamento')
print('''
      cb
      cc
      pix
''')

forma = (str(input('Qual forma de pagamento?')))
print(forma)

if forma == 'cb' or 'cc':
    print('Aproxime ou insira!')
elif forma == 'pix':
    if forma == 'pix':
        p = str(input('QR CODE ou chave pix?'))
        print(p)
        if p == 'chavepix':
            print('Chave pix produtocomdesconto@gmail.com')
        elif p == 'QR CODE':
            print('Gerando QR CODE')
        else:
            print('responda com QR CODE ou chave pix!!!')
else:
    print('tente novamente!!!')

# jeito da professora

# Peça o valor de um produto e:
# produto =  float(input('Digite o valor do produto: '))


# # Calcule um desconto de 10%.


# desconto = produto * 0.10


# # Mostre o valor final.


# valor_prod = produto - desconto
# print('Valor do produto R$', valor_prod)


# # Verifique se o valor final é maior que 100.


# print('Verifique se o valor final é maior que 100 - ', valor_prod > 100)


# # Verifique se o produto ficou barato (menor que 50).


# print('Verifique se o produto ficou barato (menor que 50) - ', valor_prod < 50)


