#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele
n1 = 5
while (n1!=0):
    n1 = (input("Digite algo : "))
    print(f"O tipo primitivo desse valor é {type(n1)}")
    print(f"Esse valor é numerico ? {n1.isnumeric()}")
    print(f"Esse valor é uma letra ? {n1.isalpha()}")
    print(f"Esse valor é um alfanuméricos ? {n1.isalnum()}")
    print(f"Esse valor é uma letra de a-z? {n1.isascii()}")
    print(f"Nesse valor, todos os digitos são digitos? {n1.isdigit()}")
    print(f"Esse valor é maiusculo ? {n1.isupper()}")
    print(f"Esse valor é minusculo ? {n1.lower()}")
