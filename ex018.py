#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cossego e tangente desse angulo
import math
angulo=float(input('Digite o valor do angulo: '))

print(f'O valor do cosseno do angulo {angulo} é {math.cos(math.radians(angulo)):.2f}')
print(f'O valor do seno do angulo {angulo} é {math.sin(math.radians(angulo)):.2f}')
print(f"O valor da tangente do angulo {angulo} é {math.tan(math.radians(angulo)):.2f}")

