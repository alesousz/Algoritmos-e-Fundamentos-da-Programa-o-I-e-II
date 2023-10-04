# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
somadorhomem = 0
somadoridade = 0
somadormulher = 0

while True:
    print('CADASTRE UMA PESSOA')
    idade = int(input('Idade: '))

    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    if sexo not in ['M', 'F']:
        print('Por favor, digite um sexo valido [M/F]')
        continue
    if idade < 20 and sexo == 'F':
        somadormulher += 1

    if sexo == 'M':
        somadorhomem += 1

    if idade > 18:
        somadoridade += 1


    pergunta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    if pergunta not in ['S', 'N']:
        print('Por favor digite um valor correto [S/N] ')
        continue

    if pergunta == 'N':
        break




print(f'Existem {somadormulher} mulheres registradas no sistema com menos de 20 anos')
print(f'Existem {somadorhomem} homens registrados no sistema')
print(f'Existem {somadoridade} pessoas maiores de 18 anos')
