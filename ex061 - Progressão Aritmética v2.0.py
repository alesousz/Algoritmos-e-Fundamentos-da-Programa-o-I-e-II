#Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
#termo
numero = int(input('Digite um numero: '))
razão = int(input('Digite a razão: '))
numero_atualizado = numero
cont = 1
while cont <= 10:
    print(f"{numero_atualizado}", end=" ")
    numero_atualizado = numero_atualizado + razão
    cont = cont + 1




