n1 = float(input('primeira nota :'))
n2 = float(input('segunda nota: '))
n3 = float(input('terceira nota: '))
media = (n1 + n2 + n3/3)
media_de_apro = (n1 +n2*2+n3 + media/7)
if media_de_apro >= 9.0:
    print('A MEDIA DE APROVEITAMENTO (A)')
elif media_de_apro > 7.5  < 9.0:
    print('A MEDIA DE APROVEITAMENTO (B)')
elif media_de_apro >= 6.0  < 7.5:
    print('A MEDIA DE APROVETAMENTO (C)')
else:
    media_de_apro < 6.0
    print('A MEDIA DE APROVEITAMENTO (D)')


