#Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
# mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
acumulador = 0
contador = 0
idades = []
for pessoas in range (1,5):
    print(f'{pessoas}° PESSOA')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    acumulador += idade
    media = acumulador/pessoas
    idades.append(idade)
    maisvelho = max(idades)

print(f'A media das idades das pessoas é {media}')
print(f'O homem mais velho se chama {nome} e tem {maisvelho} anos')
print('{} mulheres tem menos de 20 anos')