x=1
while x==1:
    print('C A L C U L A R    P R E S T A M O')
    monto=int(input('¿Cuál es el monto a prestar? '))
    tiempo=int(input('¿A cuantos años se realizara el prestamo? '))*12
    interes=float(input('¿Cuál es el interes mensual al que se hara el prestamo? '))/100

    pago=[i for i in range(1,tiempo+1)]

    Abono_Fijo=monto/tiempo
    saldo=monto
    Saldo_debido=[monto]
    for j in pago[1:]:
        saldo=saldo-Abono_Fijo
        Saldo_debido.append(saldo)
               
    Inte_Mens=[interes*x for x in Saldo_debido]
    Pago_Mens=[Abono_Fijo+y for y in Inte_Mens]

    Deuda_Total=int(sum(Pago_Mens))
    Pago_Fijo_Mensual=int(sum(Pago_Mens)/tiempo)
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