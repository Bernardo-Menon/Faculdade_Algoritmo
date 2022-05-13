posicoes_tabuleiro = {'A1': 'A1', 'A2': 'A2', 'A3': 'A3',
                      'B1': 'B1', 'B2': 'B2', 'B3': 'B3',
                      'C1': 'C1', 'C2': 'C2', 'C3': 'C3'}
simbolo1 = 'X '
simbolo2 = 'O '

def TABULEIRO():
    print('\n {} |  {}  | {} \n'
          '————┼——————┼————— \n'
          ' {} |  {}  | {} \n'
          '————┼——————┼————— \n'
          ' {} |  {}  | {} \n'
          .format(posicoes_tabuleiro['A1'], posicoes_tabuleiro['A2'], posicoes_tabuleiro['A3'],
                  posicoes_tabuleiro['B1'], posicoes_tabuleiro['B2'], posicoes_tabuleiro['B3'],
                  posicoes_tabuleiro['C1'], posicoes_tabuleiro['C2'], posicoes_tabuleiro['C3']))


def jogada_completa(jogador):
    while True:
        jogada = input(f'{jogador} digite sua jogada: ').upper()
        # Verificar se o input é válido
        if jogada not in jogadas_validas:
            print('\nVocê escolheu uma opção INVÁLIDA... Tente novamente')
        else:
            # Verificar se a posição escolhida está "vazia"
            if posicoes_tabuleiro[jogada] == simbolo1 or posicoes_tabuleiro[jogada] == simbolo2:
                print('\nVocê escolheu uma opção INDISPONÍVEL... Tente novamente')
            else:
                simbolo_usado = 0
                # Verificar qual é o jogador e setar seu simbolo
                if jogador == jogador1:
                    simbolo_usado = simbolo1
                else:
                    simbolo_usado = simbolo2
                # Preencher a posição escolhida com o simbolo do jogador1 e exibir o tabuleiro
                posicoes_tabuleiro[jogada] = simbolo_usado
                TABULEIRO()
                break # Sair do while da jogada


print('\n-----BEM VINDO AO JOGO DA VELHA-----')
jogador1 = str(input('Jogador 1, digite seu nome: '))
jogador2 = str(input('Jogador 2, digite seu nome: '))
jogadores = (jogador1, jogador2, 'Empate')

ganhador = ''
jogadas_validas = ('A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3')

TABULEIRO()

while ganhador not in jogadores:
    jogada_completa(jogador1)
    # Verificar se o jogador 1 ganhou!
    if (posicoes_tabuleiro['A1'] == simbolo1 and posicoes_tabuleiro['A2'] == simbolo1 and posicoes_tabuleiro['A3'] == simbolo1) or (
            posicoes_tabuleiro['B1'] == simbolo1 and posicoes_tabuleiro['B2'] == simbolo1 and posicoes_tabuleiro['B3'] == simbolo1) or (
            posicoes_tabuleiro['C1'] == simbolo1 and posicoes_tabuleiro['C2'] == simbolo1 and posicoes_tabuleiro['C3'] == simbolo1) or (
            posicoes_tabuleiro['A1'] == simbolo1 and posicoes_tabuleiro['B2'] == simbolo1 and posicoes_tabuleiro['C3'] == simbolo1) or (
            posicoes_tabuleiro['C1'] == simbolo1 and posicoes_tabuleiro['B2'] == simbolo1 and posicoes_tabuleiro['A3'] == simbolo1):
        ganhador = jogador1
    else:
        # Verificar se a partida empatou! (Jogador 1 sempre fará a última jogada)
        posicoes_vazias = list()
        # Para cada posição no tabuleiro, verificar se o valor corresponde aos simbolos1/simbolo2 
        for k, v in posicoes_tabuleiro.items():
            if v == simbolo1 or v == simbolo2:
                posicoes_vazias.append(0)
            else:
                posicoes_vazias.append(1)
        # Se a soma da lista for 0 significa que nenhuma posição no tabuleiro está "vazia"
        if sum(posicoes_vazias) == 0:
            ganhador = 'Empate'
        else:
            jogada_completa(jogador2)
            # Verificar se o jogador 2 ganhou!
            if (posicoes_tabuleiro['A1'] == simbolo2 and posicoes_tabuleiro['A2'] == simbolo2 and posicoes_tabuleiro['A3'] == simbolo2) or (
                    posicoes_tabuleiro['B1'] == simbolo2 and posicoes_tabuleiro['B2'] == simbolo2 and posicoes_tabuleiro['B3'] == simbolo2) or (
                    posicoes_tabuleiro['C1'] == simbolo2 and posicoes_tabuleiro['C2'] == simbolo2 and posicoes_tabuleiro['C3'] == simbolo2) or (
                    posicoes_tabuleiro['A1'] == simbolo2 and posicoes_tabuleiro['B2'] == simbolo2 and posicoes_tabuleiro['C3'] == simbolo2) or (
                    posicoes_tabuleiro['C1'] == simbolo2 and posicoes_tabuleiro['B2'] == simbolo2 and posicoes_tabuleiro['A3'] == simbolo2):
                ganhador = jogador2

if ganhador == 'Empate':
    print('A partida Empatou!')
else:
    print(f'Parabéns {ganhador}, você venceu essa partida!')