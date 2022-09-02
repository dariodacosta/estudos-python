notas = [6,7,5,8,9,10,6,10,10]
soma = 0 
x = 0
while x < len(notas):
    soma = soma + notas[x] 
    x += 1
print(f'media: {soma / x}')
print(x)