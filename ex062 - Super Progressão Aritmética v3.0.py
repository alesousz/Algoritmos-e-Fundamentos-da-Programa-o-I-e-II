# Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
numero = int(input('1° termo: '))
razão = int(input('Razão: '))
numero_atualizado = numero
cont = 1
usuario = 1
while usuario != 0:
    while cont <= 10:
        print(f'{numero_atualizado}', end=" ")
        cont += 1
        numero_atualizado = numero_atualizado + razão
    print()
    usuario = int(input('Digite quantos termos a mais quer mostrar: '))
    cont2 = 1
    if usuario == 0:
      print('FIM')
    else:
      while cont2 <= usuario:
        print(f'{numero_atualizado}', end=" ")
        cont2 += 1
        numero_atualizado = numero_atualizado + razão



