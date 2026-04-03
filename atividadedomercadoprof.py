

# Uma loja oferece um cupom especial. O cliente ganha 
# o cupom se atender a pelo menos  das seguintes condições:
# Se for VIP (responde "sim" ou "não") vip:
# Valor da compra acima de R$ 200 valor_c?
# Primeira compra no mês (responder "sim" ou "nao") compra_mes
# Além disso, o cupom  pode ser aplicado se o cliente tiver  
# no histórico 


loja = {


    'clientes':
        {
            'junior':{
                'vip': 'sim',
                'compra':201.0,
                'primeira_compra':'sim',
                'reclamacao':False


            },
            'fernando':{
                'vip': 'não',
                'compra':500.0,
                'primeira_compra':'não',
                'reclamacao':True
            }
        }}



nome = input('Nome: ')
# vip = input('É cliente VIP? ')
# valor_compra  =  float(input('Valor da compra R$ '))
# primeira_compra  =  input('Primeira compra sim ou não: ')
# reclamacao =  bool(input('Possui reclamação? '))


verificar_vip  =   loja['clientes'][nome]['vip'] == 'sim'
print(verificar_vip)
verifica_valor  =  loja['clientes'][nome]['compra'] > 200
print(verifica_valor)
verificar_p_compr =  loja['clientes'][nome][''] == 'sim'
print(verificar_p_compr)
recla = loja['clientes'][nome]['reclamacao']  == False
print(recla)


saida = verificar_vip and verifica_valor and verificar_p_compr and recla and "Cupom liberado" or 'sem cupom'


print(saida)

