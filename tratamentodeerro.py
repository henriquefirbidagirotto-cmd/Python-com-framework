# try:
#    tente fazer isso 
# except:
#    isso não funcionar mostre 
# else:
#    erro não identificado
# finally:
#    sempre carrega   




# var =  10
# x =  100


# indentação  = organzação do código


try:
    x  =  float(input('>>>'))
    print(10 + x)
    
except NameError:
    print('essa variavel não foi criada')
except ValueError:
    print('Digite o dado correto de acordo com o input')
except TypeError:
    print('Calculo aritmético entre texto e numero')      
    
else:
    print('ocorreu um não identificado ou não houve erro')
   
finally:
    print('fim  decarregamento...')











try:
    x  =  float(input('>>>'))
    print(10 + x)
    
except NameError as erro:
    print(erro)
except ValueError as erro:
    print(erro)
except TypeError as erro:
    print(erro)      
    
else:
    print('ocorreu um não identificado ou não houve erro')
   
finally:
    print('fim  decarregamento...')