import time

numero = float(input("Digite um numero inteiro positivo:"))
resto = numero % 2 

if (resto == 0):
    print('"P-A-R!!!"')

else:
    print("Tente Outra vez!")

time.sleep(5)