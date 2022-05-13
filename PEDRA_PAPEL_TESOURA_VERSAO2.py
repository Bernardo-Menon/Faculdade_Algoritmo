from random import *


print('-'*25)
print('PEDRA, PAPEL E TESOURA')
print('-'*25)

jogador1 = input('\nJogador 1, digite seu nome: ')
jogador2 = 'Máquina'

print('\n[1] - Pedra\n[2] - Papel\n[3] - Tesoura')

opcoes = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}

mensagem_erro = ('\n\033[31m' + 'Você digitou uma opção inválida' + '\033[0;0m')

jogada1 = int(input(f'\n{jogador1} digite uma opção: '))
if jogada1 not in opcoes:
    print(mensagem_erro)
else:
    jogada2 = randint(1,3)    
    if jogada1 == jogada2 or jogada2 == jogada1:
        print('A partida empatou')
    else:
        if jogada1 == 1: #jogador 1 colocando a opção 1 (Pedra)
            if jogada2 == 2: #jogador 2 colocando a opção 2 (Papel)
                ganhador = jogador2
            else: #jogador 2 colocando a opção 3 (Tesoura)
                ganhador = jogador1
        else:
            if jogada1 == 2: #jogador 1 colocando a opção 2 (Papel)
                if jogada2 == 1: #jogador 2 colocando a opção 1 (Pedra)
                    ganhador = jogador1
                else: #jogador 2 colocando a opção 3 (Tesoura)
                    ganhador = jogador2
            else: #jogador 1 colocando a opção 3 (Tesoura)
                if jogada2 == 1: #jogador 2 colocando a opção 1 (Pedra)
                    ganhador = jogador2
                else: #jogador 2 colocando a opção 2 (Papel)
                    ganhador = jogador1
        print(f'\nComo {jogador1} escolheu {opcoes[jogada1]} e {jogador2} escolheu {opcoes[jogada2]}')
        print(f'Parabéns {ganhador}! Você ganhou a partida!')
