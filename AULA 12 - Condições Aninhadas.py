#CONDIÇÃO ANINHADAS
#if condição:
#elif condição:
#else:
nome = input('Qual é o seu nome ?')
if nome == 'Gustavo':
    print('Que nome bonito')
elif nome == 'Pedro' or 'Maria' or 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é normal')

print(f'Tenha um bom dia, {nome}!')

