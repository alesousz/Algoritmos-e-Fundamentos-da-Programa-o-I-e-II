#Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.
tupla = ('Botafogo', 'Palmeiras', 'Flamengo', 'Atletico Mineiro', 'Fluminense', 'São Paulo', 'Grêmio', 'Fortaleza', 'Athletico Paranaense', 'Cruzeiro', 'Internacional', 'Bragantino', 'Santos', 'Bahia', 'Corinthians', 'Cuiabá', 'Goiás', 'America Mineiro', 'Vasco da Gama', 'Coritiba')

#a) Os 5 primeiros times.
print(f'Os primeiros cinco times na Tabela do Campeonato Brasileiro de Futebol são:')
for time in tupla[0:5]:
    print(f'{time}', end=',')
print('\n','-=' * 15)

#b) Os últimos 4 colocados.
print(f'Os ultimos quatro colocados são: ')
for time in tupla[16:]:
    print(f'{time}', end=',')
print('\n','-=' * 15)

#c) Times em ordem alfabética.
print('Times em ordem alfabética são: ')
for time in sorted(tupla):
    print(f'{time}', end=',')
print('\n','-=' * 15)

#d) Em que posição está o time da Chapecoense.
print('Em que posição está o time do Flamengo?', end=' ')
print(f"A posição do Flamengo no campeonato é: {tupla.index('Flamengo')+1}° lugar")
