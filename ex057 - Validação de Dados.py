#Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

while True:
    s = str(input('Digite seu sexo[M/F]: ')).upper().strip()
    if s == 'M' or s == 'F':
        #if s in ['M', 'F']: PODE USAR ISSO AQUI, QUE ELE VE DENTRO DA LISTA SE A RESPOSTA É UMA OU OUTRA
        print(f'Sexo {s} registrado ')
        break
    else:
        print('Valor incorreto! Tente novamente')





