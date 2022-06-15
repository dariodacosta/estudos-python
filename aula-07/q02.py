h1 = int(input('idade: '))
h2 = int(input('idade: '))
m1 = int(input('idade: '))
m2 = int(input('idade: '))
if h1>h2 and m1>m2:
    soma = h1 + m2
    produto = h2 * m1
    print('A soma  e o produto das idades era: ')
elif h1>h2 and m2>m1:
    soma = h1 + m1
    produto = h2 * m1
    print('A soma e o produto das idades sera: ')
elif h2>h1 and m2>m1:
    soma = h1+m1
    produto = h2 * m2
    print('A soma e o produto das idades sera: ')
else:
    print('A Soma e o produto das idade sera : ')    