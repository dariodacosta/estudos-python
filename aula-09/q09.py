a = 5
b = 3
c = 3
if (a < b + c) and (b < a + c) and (c < a + b):
    print('Equilatero')
elif (a==b) or (b==c) or (a==c):
    print('Isósceles')
else:
    print('Escaleno')