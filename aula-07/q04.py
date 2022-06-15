usuario = int(input('Digite o codigo: '))
senha = int( input('Digite a senha: '))
if senha == usuario:
    print('USUARIO INVALIDO')
elif usuario == senha:
    print('SENHA INCORRETA')
else:
    print('ACESSO PERMITIDO')