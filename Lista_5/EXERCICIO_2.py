# Lista 5 - Funções
# Exercício 2 - Faça uma função que recebe a média final de um aluno por parâmetro e retorna o seu conceito, conforme a tabela abaixo: 
#    Conceito    Nota 
#    D           De 0 a 49
#    C           De 50 a 69
#    B           De 70 a 89
#    A           De 90 a 100

def calculo_conceito (media):
    if media >= 90:
        conceito = 'A'
    else:
        if media >= 70:
            conceito = 'B'
        else:
            if media >= 50:
                conceito = 'C'
            else:
                conceito = 'D'
    return conceito


media_aluno = float(input("Digite qual foi a média do aluno: "))
print(f'O aluno está classificado no conceito: {calculo_conceito(media_aluno)}')