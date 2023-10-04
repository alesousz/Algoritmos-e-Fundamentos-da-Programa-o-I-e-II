#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e motre o comprimento da hipotenusa
from math import hypot
cateto_oposto=float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente=float(input('Digite o comprimento do caceto adjacente: '))
print(f'O comprimento da tangente é de {hypot(cateto_adjacente,cateto_oposto):.2f}')
#OU USANDO A FORMULA MATEMATICA

cateto_oposto=float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente=float(input('Digite o comprimento do cateto adjacente: '))
hi=(cateto_oposto**2 + cateto_adjacente**2)**(1/2)
print(f'A soma do cateto oposto e do catete adjacente é {hi} ')
