# Sabendo que A=3, B=7 e C=4, informe se as expressões abaixo são (T) para verdadeiras
# ou (F) falsas.
# a) (A+C) > B ( )
# b) B >= (A + 2) ( )
# c) C = (B –A) ( )
# d) (B + A) <= C ( )
# e) (C+A) > B ( )
a = bool(input(' A=: '))
b = bool(input(' B=: '))
c = bool(input(' C=: '))

print('a): ' , (a+c)>b)
print('b): ' , (b>=(a+2))) 
print('c): ' , (c==(b-a))) 
print('d): ' , (b+a)<=c)  
print('e): ' , (c+a)>b)