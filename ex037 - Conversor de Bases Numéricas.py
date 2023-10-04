#Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
print('Bem-vindo ao conversor de bases !')

print('[1] BINARIA')
print('[2] OCTAL')
print('[3] HEXADECIMAL')
conversão = int(input('Qual tipo de conversão deseja realizar?'))
if conversão == 1:
    numero = int(input('Qual numero quer converter ?'))
    print(f'O valor em binario é {bin(numero)[2:]}')
elif conversão==2:
    numero = int(input('Qual numero quer converter ?'))
    print(f'O valor informado ém octal é {oct(numero)[2:]}')
elif conversão==3:
    numero = int(input('Qual numero quer converter ?'))
    print(f'O valor informado em hexadecimal é {hex(numero)[2:]}')
else:
    print('Valor incorreto, tente novamente')