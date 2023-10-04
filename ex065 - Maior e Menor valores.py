#Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
soma = cont = 0
parar = 0
lista = []
while parar != str('S'):
    n = int(input('Digite um numero: '))
    lista.append(n)
    soma += n
    cont += 1
    parar = str(input('DESEJA PARAR ? [S/N] ')).upper()
    maior = max(lista)
    menor = min(lista)
media = soma / cont
print(f'Você digitou {cont} numeros. A media entre os numeros mostrados é {media}')
print(f'O maior valor informado foi {maior} e o menor foi {menor}')