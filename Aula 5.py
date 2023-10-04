#Quando queremos acrescentar informações importantes dentro de uma variavel, como dar um espaço
#ou queremos centralizar e assim por diante fazemos da seguinte forma:
nome = input('Qual é o seu nome ?')
print(f'Prazer em te conhecer {nome:=^20}')
#Ou seja, apos colocarmos a variavel dentro dos {} acrescentamos um ":" e em seguida as informações
#Nesse exemplo, eu pedi que o python apresentasse o nome dentro de 20 espaços, como o nome não tem tudo isso
#de letras, coloquei um sinal de = que preencheu o resto do espaço disponivel, já o ^ centraliza o nome, assim
#o nome informado no input fica no meio e o resto é preenchido pelo =
#------------------------------------------------------------------------------------------------------------
#Linhas com print
#Podemos manter prints na mesma linha seguindo a forma abaixo
print('Hello World!', end=" "),
print('Tudo bem com você?')
#Tambem podemos quebrar prints em linhas :
print('Qual é o seu nome ? \nTudo bem com você ? \nComo está se sentindo hoje?')
#----------------------------------------------------------------------------------------------------------