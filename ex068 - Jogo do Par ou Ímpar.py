#Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
#O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
cont = 0
while True:
    escolha = str(input('PAR OU IMPAR? [P/I]: '))
    numero = int(input('DIGITE UM NUMERO: '))
    pc = randint(0, 10)
    cont += 1
    if escolha in 'Pp':
        pc = randint(0, 10)
        soma = numero + pc
        if soma % 2 == 0:
            print(f'VOCÊ JOGOU {numero} e o computador {pc}. O total deu {soma} - DEU PAR')
            print('Você VENCEU! Vamos jogar novamente!')
        elif soma % 2 != 0:
            print(f'VOCÊ JOGOU {numero} e o computador {pc}. O total deu {soma} - DEU IMPAR')
            print('Você PERDEU! Programa encerrado!')
            break
    elif escolha in 'Ii':
        pc = randint(0, 10)
        soma = numero + pc
        if soma % 2 != 0:
            print(f'VOCÊ JOGOU {numero} e o computador {pc}. O total deu {soma} - DEU IMPAR')
            print('Você VENCEU! Vamos jogar novamente!')
        elif soma % 2 == 0:
            print(f'VOCÊ JOGOU {numero} e o computador {pc}. O total deu {soma} - DEU PAR')
            print('Você PERDEU! Programa encerrado!')
            break
print(f'GAME OVER ! Você venceu {cont-1} vezes')

#ESCOLHER PAR OU IMPAR
#ESCOLHER UM NUMERO
#SOMAR OS NUMEROS
#CHECAR SE O RESULTADO DA SOMA É PAR OU IMPAR
#AI DPS VARIOS IFS SE FOR UM OU OUTRO