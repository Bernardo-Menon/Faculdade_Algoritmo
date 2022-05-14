# Lista 5 - Funções
# Exercício 1 - Faça uma função que recebe a idade de uma pessoa em anos, meses e dias e retorna essa idade expressa em dias.

from datetime import date

# Fazendo de forma genérica. Sem tratativa de ano bissexto e dias do mês
# ano = 365 dias
# mês = 30 dias  

def dias_vividos(d, m, a):
    ano_em_dias = ((today.year - a) - 1) * 365 # Ano de hoje - ano do nascimento = idade (Retirado 1 ano, pois o ano atual calcularemos os dias somente até a data atual)
    mes_em_dias_ano_nascimento = (12 - m) * 30 # meses do ano - mês de nascimento = meses completos vividos no ano de nascimento (Ex.: Nascido no mês 10 (12-10=2), viveu o mês 11 e 12 por completo no ano de nascimento)
    mes_em_dias_ano_atual = (today.month - 1) * 30 # Calcular quantos meses viveu no ano atual sem considera o mês atual (Que não foi completo ainda) 
    dias_no_mes_nascimento = (30 - d) # Calcular quantos dias viveu no mês atual 
    dias_vividos = [ano_em_dias, mes_em_dias_ano_nascimento, mes_em_dias_ano_atual, dias_no_mes_nascimento, today.day] # Tupla com todos os cálculos
    return sum(dias_vividos) # Soma de todos os itens da Tupla

today = date.today() # Definir data atual

dia = int(input("Em qual dia você nasceu? "))
mes = int(input("Em qual mês você nasceu? "))
ano = int(input("Em qual ano você nasceu? "))

print(f'\nSendo a data de hoje: {"%02d" % (today.day)}/{"%02d" % (today.month)}/{today.year} \nVocê já viveu, aproximadamente, {dias_vividos(dia, mes, ano)} dias.')
# {"%02d" % (today.day)} Essa formatação trará o 0 a esquerda quando necessário.