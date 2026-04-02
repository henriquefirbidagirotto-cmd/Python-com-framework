# Contexto:
# Uma indústria monitora temperatura (T), umidade (U) e presença de gás inflamável (G, 0 ou 1).
# O nível de risco é dado por:

# Crítico: (T > 40 ou U > 80) e G == 1

# Alto: (T > 40 ou U > 80) e G == 0

# Médio: (T entre 25 e 40) e (U entre 50 e 80)

# Baixo: qualquer outra situação

# Tarefa:
# Receba T (float), U (float), G (0 ou 1).
# Classifique o risco em "Crítico", "Alto", "Médio" ou "Baixo" sem usar if/elif.
# Use apenas dicionários com chaves booleanas e operadores lógico

# UTILIZE APENAS SINAIS LÓGICOS -  VARIAVEIS  -  LISTAS  -  I/O -  NÃO UTILIZE CONDICIONAIS OU LOOPS

print('''
    Monitoramento de risco
      Gás 1 para sim e 0 para não
''')

t = float(input('Temperatura: '))
u = float(input('Umidade: '))
g = int(input('Gás inflamavel: '))

cri = t >=40 and u >=80 and g == 1
cr = cri == True and print('Risco Critico!')

Alt = t >= 40 and u >= 80 and g == 0
al = Alt == True and print('Risco Alto')

med = (t >= 25 and t <= 40) and (u >= 50 and u <= 80)
me = med == True and print('Risco Medio')

bai = not med == True and not Alt == True and not cri == True and print('Risco Baixo')