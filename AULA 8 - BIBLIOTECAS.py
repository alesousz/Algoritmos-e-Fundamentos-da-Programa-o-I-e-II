#Existem duas maneiras de se importar modulos em python.
#Existe o: import bebidas - para importar uma biblioteca inteira de funções no python
#E existe o: from bebidas import agua - quando queremos importar somente alguma FUNÇÃO especifica da biblioteca BEBIDAS
#Nesse segundo caso, mais especifico, podemos importar mais de uma FUNÇÃO utilizando a VIRGULA :
#EXEMPLO from bebidas import agua,refrigerante

#importando toda a biblioteca
import math
numero=int(input('Digite um numero: '))
raiz=math.sqrt(numero)
#na função print abaixo vemos que para utilizar o math dentro do f {}, podemos so jogar o math.tralala(variavel)
print(f'A raiz de {numero} é igual a {math.ceil(raiz)} arredondada para cima e {math.floor(raiz)} arredondada para baixo')

#IMPORTANDO FUNÇÕES ESPECIFICAS DE UMA BIBLIOTECA
from math import sqrt

numero=int(input('Digite um numero: '))
#VEMOS QUE QUANDO IMPORTAMOS SOMENTE ALGO ESPECIFICO NÃO PRECISAMOS USAR O MATH, DIFERENTE DO EXEMPLO ACIMA
raiz=sqrt(numero)
print(f'A raiz quadrada de {numero} é {sqrt(numero):.2f} ')

#NOS DOIS TESTE O RESULTADO É DIFERENTE POR QUE USAMOS MATH.CEIL PARA ARREDONDAR O RESULTADO PARA CIMA, PORÉM É O MESMO CODIGO
import emoji
print(emoji.emojize('Ola Mundo :globe_showing_Americas:', language = 'alias' ))