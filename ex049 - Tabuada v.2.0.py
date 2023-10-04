#049 - TabuExercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.
tab = int(input('Digite um numero: '))
for c in range(0, 11):
    print(f'{tab}x{c}={tab*c}')