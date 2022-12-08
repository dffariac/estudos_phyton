usuarios = []


if usuarios: 
    for usuario in usuarios:
     if usuario == 'admin' : print ('\nOlá,' + usuario.title() + ' gostaria de alterar algo?')
     elif usuario != 'admin' : print ("\nOlá, seja bem vindo " + usuario.title())
     else: print ("Adicione novos usuários")