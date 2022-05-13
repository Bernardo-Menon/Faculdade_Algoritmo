print('-'*25)
print('PEDRA, PAPEL E TESOURA')
print('-'*25)

jogador1 = input('\nJogador 1, digite seu nome: ')
jogador2 = input('Jogador 2, Digite seu nome: ')

print('\n[1] - Pedra\n[2] - Papel\n[3] - Tesoura')

opcoes = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}

mensagem_erro = ('\n\033[31m' + 'Você digitou uma opção inválida' + '\033[0;0m')

jogada1 = int(input(f'\n{jogador1} digite uma opção: '))
if jogada1 not in opcoes:
    print(mensagem_erro)
else:
    jogada2 = int(input(f'\n{jogador2} digite uma opção: '))
    if jogada2 not in opcoes:
        print(mensagem_erro)
    else:
        if jogada1 == jogada2 or jogada2 == jogada1:
            print('A partida empatou')
        else:
            # Jogador 1 colocando a opção 1 (Pedra)
            if jogada1 == 1: 
                # Jogador 2 colocando a opção 2 (Papel)
                if jogada2 == 2: 
                    ganhador = jogador2
                # Jogador 2 colocando a opção 3 (Tesoura)
                else: 
                    ganhador = jogador1
            else:
                # Jogador 1 colocando a opção 2 (Papel)
                if jogada1 == 2: 
                    # Jogador 2 colocando a opção 1 (Pedra)
                    if jogada2 == 1: 
                        ganhador = jogador1
                    # Jogador 2 colocando a opção 3 (Tesoura)
                    else: 
                        ganhador = jogador2
                # Jogador 1 colocando a opção 3 (Tesoura)
                else: 
                    # Jogador 2 colocando a opção 1 (Pedra)
                    if jogada2 == 1: 
                        ganhador = jogador2
                    # Jogador 2 colocando a opção 2 (Papel)
                    else: 
                        ganhador = jogador1            
            print(f'\nComo {jogador1} escolheu {opcoes[jogada1]} e {jogador2} escolheu {opcoes[jogada2]}')
            print(f'Parabéns {ganhador}! Você ganhou a partida!')