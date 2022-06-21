a = int(input('LADO 1: '))
b = int(input('LADO 2: '))
c = int(input('LADO 3: '))
if (a == 90) or (b == 90) or (c == 90):
    print('RETANGULO')
elif (a > 90) or (b > 90) or (c > 90):
    print('OBTUSANGULO')
else:
    print('ACUTANGULO')      