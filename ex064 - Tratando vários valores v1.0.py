#Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n = 0
cont = 0
soma = 0
n = int(input('Digite um numero [999 para parar]: '))
while n != 999:
    cont += 1
    soma = n + soma
    n = int(input('Digite um numero [999 para parar]: '))
print(f'Você digitou {cont} numeros e a soma entre eles foi {soma}.')

#NESSE EXERCICIO A REPETIÇÃO DO N OCORRE DENTRO E FORA. POR QUE ? POR QUE ASSIM PODEMOS USAR O INPUT NORMALMENTE E ASSIM QUE DIGITAMOS O 999 O LUP PARA
#DESSE MODO ELE N É INCLUIDO NA CONTAGEM DO CONT E NEM NA SOMA