#Um programa que lê um numero e mostra o seu dobro, triplo e raiz quadrada
valor = int(input('Digite um valor: '))
dobro = int(valor*2)
triplo = int(valor*3)
raiz = float(valor**(1/2))
print(f'O dobro de {valor} é {dobro}. \nO triplo de {valor} é {triplo}. \nA raiz quadrada de {valor} é {raiz:.2f}.') # ACRESCENTEI O PONTO + A QUANTIDADE DA CASAS DECIMAIS Q QUERIA E O F DE FLOAT