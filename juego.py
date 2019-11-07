import random
AC= ["BANCO" ,"INVERSIONES TEMPORALES", "CLIENTES", "DEUDORES DIVERSOS" ,"DOCUMENTOS POR COBRAR","INVENTARIO ALAMACEN","PAGOS ANTICIPADOS"]
ANC=["TERRENOS","EDIFICIOS","MOVILIARIO","EQUIPO DE TRANPORTE", "EQUIPO DE COMPUTO "]
PCP=["PROVEDORES","ACREDORES DIVERSOS","DOCUMENTOS POR PAGAR","PRESTAMOS BACARIOS A CORTO PLAZO","COBROS ANTICIPADOS"]

def main():
    x, y = aletorio()
    print(x,y)
    dec=leer()
    print("Que tipo de cargo es \n ",dec)


def vof(dec):
    if dec==ACTIVOS 

def leer():
    y=str(input("Que tipo de cargo es ")).upper()
    return y

def aletorio():
    y=random.randrange(2)
    if y==0:
        x=random.randrange(len(AC))
        print(AC[x])
    elif y==1:
        x=random.randrange(len(ANC))
        print(ANC[x])
    else:
        x=random.randrange(len(PCP))
        print(PCP[x])
    return x,y
if __name__=='__main__':
    main()



"""
C=str(input("Dame un array")).upper()
if C in AC: # Imprime lo de abajo
    print("CORRECTO")
else:
    print("Falso")
"""
