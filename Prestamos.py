x=1
while x==1:
    monto=int(input('¿Cuál es el monto a prestar? '))
    tiempo=int(input('¿A cuantos años se realizara el prestamo? '))
    tiempo=tiempo*12
    interes=float(input('¿Cuál es el interes mensual al que se hara el prestamo? '))
    interes=interes/100

    pago=[]
    for i in range(1,tiempo+1):
        pago.append(i)

    Abono_Fijo=monto/tiempo
    saldo=monto
    Saldo_debido=[monto]
    for j in pago[1:]:
        saldo=saldo-Abono_Fijo
        Saldo_debido.append(saldo)

    Inte_Mens=[]
    for x in Saldo_debido:
        I_M=interes*x
        Inte_Mens.append(I_M)

    Pago_Mens=[]
    for y in Inte_Mens:
        suma=Abono_Fijo+y
        Pago_Mens.append(suma)

    for n in Pago_Mens:
        Pago_Fijo_Mensual=sum(Pago_Mens)
        Deuda_Total=int(Pago_Fijo_Mensual)
    Pago_Fijo_Mensual=int(Pago_Fijo_Mensual/tiempo)
    Pago_Fijo_Quincenal=int(Pago_Fijo_Mensual/2)

    print('\n')
    print('El monto prestado es de $'+ str(monto))
    print('\n')
    print('Por un tiempo de ' + str(tiempo) + ' meses')
    print('\n')
    print('Con un interes mensual del '+str(interes*100)+'%')
    print('\n')
    print('La deuda total asciende a $'+str(Deuda_Total))
    print('\n')
    print('El pago fijo mensual es de $' + str(Pago_Fijo_Mensual))
    print('\n')
    print('El pago fijo quincenal es de $'+ str(Pago_Fijo_Quincenal))
    print('\n')
    
    seguir=input('¿Quieres realizar otra consulta? s/n ').lower()
    if seguir=='n':
        x=0
    else:
        x=1