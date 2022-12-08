age = 28

if age < 2 : print("Você é um bebê") 
elif age >= 2 and age < 4 : print("Você é uma criança")
elif age >= 4 and age < 13 : print("Você é um pré-adolescente")
elif age >= 13 and age < 20 : print("Você é um adolescente")
elif age >= 20 and age < 65 : print("Você é um adulto")
else: print("Você é um idoso")

age = 38

if age < 2 : frase = "Você é um bebê"
elif age >= 2 and age < 4 : frase = "Você é uma criança"
elif age >= 4 and age < 13 : frase = 'Você é um pré-adolescente'
elif age >= 13 and age < 20 : frase = "Você é um adolescente"
elif age >= 20 and age < 65 : frase = "Você é um adulto"
else: frase = "Você é um idoso" 

print ( "\n Sua idade é " + str(age) + " então " + frase)


