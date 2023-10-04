#Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.
cont = 0
while True:
    numero = int(input('Digite um numero: '))
    if numero < 0:
        break
    while cont < 10:
        cont += 1
        tabuada = numero * cont
        print(f'{numero}x{cont}={tabuada}')
    cont = 0
print('PROGRAMA ENCERRADO')
