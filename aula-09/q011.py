numb = int(input('leia um numero: '))
contador = 0
for n in range (1,numb):
   if numb % n == 0:
     contador = contador+1

if contador > 2:
   print('nao e primo')

else:
    print('e primo')

