NBA = {'boston':'17', 'lakers': '17', 'warriors':'7'}

for time, titulo in NBA.items() : print(time.title() + ' - Titulos : ' + titulo +'\n')  
# laço para percorrer um dicionário

NBA ['chigago'] = '6' # Como adicionar um valor em um dicionário
NBA ['spurs'] = '5'
NBA ['miami'] = '3'

for time, titulo in NBA.items() : print(time.title() + ' - Titulos : ' + titulo +'\n')
#Exibe dicionário após adicionar os novos pares de chave-valor

for time in sorted (NBA.keys()) : print(time.title())
 # Laço para organizar a exibição das chaves de um dicionário
