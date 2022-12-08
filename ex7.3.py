number = input("Informe um numero:\n")
number = int(number)
if number % 10 == 0:
    print (str(number) + " é um multiplo de dez")
else:
    print(str(number)+ " não é multiplo de dez")