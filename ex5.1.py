pizza = "queijo"

if pizza == "queijo" : print("A pizza é de " + pizza.title()) 
else: print("A pizza não é de queijo")

pizzas = [ 'queijo', 'calabresa', 'palmito', 'bauru', ' frango com catupiry',
'camarão', 'três queijos', 'brocolis', 'escarola']

for pizza in pizzas: 
    if pizza == "palmito" : print("\nA pizza é de " + pizza.upper())
    else: print("\nA pizza não é de palmito, mas temos o sabor " + pizza.title())

print('palmito' in pizzas)