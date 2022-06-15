litro = float(input('litros: '))
alc = float(input('valor: '))
gaso = float (input('valor: '))

if litro >= alc: 
    litro * alc
    print('valor pago de 3%: ' , (alc*3/100))
elif litro <= alc: 
    litro * alc    
    print('valor pago de 5%: ' , (alc*5/100))
elif litro >= gaso: 
    litro * gaso  
    print('valor pago de 4%: ' , (gaso*4/100))
else:    
    print('valor pago de 6%: ' , (gaso*6/100))