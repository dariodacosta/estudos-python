lista = []
numb =int(input('leia um numero: '))
for n in range (1,numb):
    contador = 0
    for i in range (1,n+1):
        if n % i == 0:
            contador = contador +1
    if contador > 2:
        print('nao primo \033[31m')
    else:
        print(f'\033[34m, {n}')
        lista.append(n)
print(lista)
    
