x=1

def prestamo():    
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
    

def deuda():
    print('C A L C U L A R    D E U D A')
    monto=int(input('¿Cuál fue el monto a prestado? '))
    tiempo=int(input('¿A cuantos años se realizo el prestamo? '))*12
    tiempo_q=tiempo*2
    interes=float(input('¿Cuál es el interes mensual al que se hizo el prestamo? '))/100

    pago=[i for i in range(1,tiempo+1)]

    Abono_Fijo=monto/tiempo
    saldo=monto
    Saldo_debido=[monto]
    for j in pago[1:]:
        saldo=saldo-Abono_Fijo
        Saldo_debido.append(saldo)
            
    pago_q=[w for w in range(1,tiempo_q+1)]    
    Abono_Fijo_q=Abono_Fijo/2
    saldo_q=monto
    Saldo_debido_q=[monto]
    for k in pago_q[1:]:
        saldo_q=saldo_q-Abono_Fijo_q
        Saldo_debido_q.append(saldo_q)

    pay_type=(input('¿El pago es mensual o quincenal?')).lower()
    if pay_type=='mensual':
        payments=int(input('¿cuantos pagos se han realizado?'))
        doubt=int(Saldo_debido[payments+1])
        print(f'La deuda se liquida con ${doubt}')
    elif pay_type=='quincenal':
        tiempo=tiempo*2
        payments=int(input('¿cuantos pagos se han realizado?'))
        doubt=int(Saldo_debido_q[payments+1])
        print(f'La deuda se liquida con ${doubt}')
    else:
        print('tipo de pago desconocido')
    

while x==1:
    c=1
    while c==1:
        print('--|--'*10)
        z=(input('¿Que desea hacer? \ncalcular [P]restamo \ncalcular [D]euda \n')).lower()
        print('--|--'*10)
        if z=='p':
            prestamo()
            c=0
        elif z=='d':
            deuda()
            c=0
        else:
            print('Opcion desconocida')
            c=1
        
    seguir=input('¿Quieres realizar otra consulta? s/n \n').lower()
    if seguir=='n':
        x=0
    else:
        x=1
