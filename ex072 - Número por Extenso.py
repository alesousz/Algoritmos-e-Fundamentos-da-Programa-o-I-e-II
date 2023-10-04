#Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    resposta = int(input('Digite um numero entre 0 e 20: '))
    print(f'{tupla[resposta]}')
    if resposta < 0 or resposta > 20:
        resposta = int(input('Valor incorreto! Digite um numero ENTRE 0 E 20: '))
        print(f'{tupla[resposta]}')
    if resposta == 1000:
        break
