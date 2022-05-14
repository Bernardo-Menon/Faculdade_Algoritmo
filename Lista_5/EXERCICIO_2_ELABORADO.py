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


notas_aluno = list()

while True:
    while True:
        nota = float(input("\nDigite a nota do aluno: "))
        if nota < 0 or nota > 100:
            print(f'\nVocê digitou um valor inválido')
        else:
            notas_aluno.append(nota)
            break
    while True:
        continuar = input('\n[S] Sim \n[N] Não \nDeseja cadastrar uma nova nota para o aluno? ').upper()
        if continuar not in ('S', 'N'):
            print('Você digitou uma opção inválida, tente novamente')
        else:
            break
    if continuar == 'N':
        break

media_aluno = sum(notas_aluno)/len(notas_aluno)
print(f'\nComo o aluna ficou com média: {media_aluno:.2f}. \nEle está classificado no conceito: {calculo_conceito(media_aluno)}')