# Estrutura de laço
# Variavel de controle

# EM PORTUGUES:
# laço C no intervalo(1,10):                     |
# indentação                                 |
# pega - o comando pega esta fora do laço

# EM PYTHON:
# for c in range(1,10):
# passo
# pega

# ------------------------------ PRATICA: se eu quiser repetir um print, em vez de ir colocando varios de uma vez eu posso usar o for:
print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('NO LAÇO: ')
for c in range(0, 6):
    print('Oi')
print('FIM')
print('CONTAGEM')
#SE QUISERMOS FAZER UMA CONTAGEM
for c in range(0, 6):
    print(c)
print('REPETIÇÃO AO CONTRARIO')
#SE QUISERMOS FAZER UMA CONTAGEM AO CONTRARIO ADICIONAMOS O -: O TERCEIRO TREM ALI DO LADO É PRA DAR SENTIDO PRA REPETIÇÃO,
# TIPO IR AO CONTRARIO OU PULAR NUMERO, NO EXEMPLO, O -1 É PRA IR DE UM EM UM, SE FOR -2, VAI SER DE DOIS EM DOIS
for c in range(6, 0, -1):
    print(c)
print('USANDO O INPUT')
for c in range(0, 2):
    n = int(input('Digite um numero: '))

print('OUTRO INPUT')
i = int(input('Digite o Inicio: '))
f = int(input('Digite o Fim: '))
p = int(input('Digite o pulo'))
for c in range(i, f+1, p):
    print(c)
