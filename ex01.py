#Escreva um algoritmo que gera a seguinte tabela.
x = -3
while x <= 3:
    y = (-x)**2 + 4*x - 5
    z = x**2 + 4*x + 5
    x = x + 0.5
    print(f'{x} | {y} | {z}')