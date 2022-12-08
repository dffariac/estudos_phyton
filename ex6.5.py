rios = {'egito': 'nilo', 'brasil': 'amazonas','estados unidos':'missisipi'} # Dicionário

for pais, rio in sorted(rios.items()) : print(" \nO principal rio do " + pais.title() + " é o rio "+ rio.title())

print('\nOs rios da lista são:') 
for rio in sorted(rios.values()) :  print(rio.title())