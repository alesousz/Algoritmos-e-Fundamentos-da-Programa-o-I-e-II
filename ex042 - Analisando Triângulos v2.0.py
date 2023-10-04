#Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes
n1=int(input('Primeiro segmento: '))
n2=int(input('Segundo segmento: '))
n3=int(input('Terceiro segmento: '))
if n1+n2 > n3 and n2+n3 > n1 and n3+n1>n2:
    print('Os três segmentos formam um triangulo')

    if n1==n2==n3:
        print('Os três segmentos são iguais, logo formam um triângulo EQUILATERO!')

    elif n1 == n2 != n3 or n2 == n3 != n1 or n3 == n1 != n2:
        print('Os três segmentos TEM dois lados iguais e um diferente, logo formam um triangulo ISÓSCELES!')

    elif n1 != n2 != n3 != n1:
        print('Os três segmentos são diferentes, logo formam um triangulo ESCALENO')
else:
    print('Os segmentos não podem formar um triangulo')