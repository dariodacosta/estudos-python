from calendar import c


a = int(input('lado: '))
b = int(input('lado: '))
c = int(input('lado: '))
if (a == b) and (a == c):
    print('Equilatero')
elif (a==b) or (a==c) or (b==c):
    print('Isósceles')
else:
    print('Escaleno')