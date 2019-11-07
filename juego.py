import random
AC= ["BANCO" ,"INVERSIONES TEMPORALES", "CLIENTES", "DEUDORES DIVERSOS" ,"DOCUMENTOS POR COBRAR","INVENTARIO ALAMACEN","PAGOS ANTICIPADOS"]
ANC=["TERRENOS","EDIFICIOS","MOVILIARIO","EQUIPO DE TRANPORTE", "EQUIPO DE COMPUTO "]
PCP=["PROVEDORES","ACREDORES DIVERSOS","DOCUMENTOS POR PAGAR","PRESTAMOS BACARIOS A CORTO PLAZO","COBROS ANTICIPADOS"]


def main():
    x, y = aletorio()
    dec=leer()
    elret=vof(dec)
    comp(elret,y)

def comp(res,y):
    if res==y:
        print("Felicidades")
    else:
        print("Te equivocaste")

def vof(dec):
    if dec=="ACTIVOS CIRCULANTES":
        print("ACTIVOS")
        elret=0
    elif dec=="ACTIVOS NO CIRCULANTES":
        print("ACTIVOS NO CIRCULANTES")
        elret=1
    elif dec=="PASIVOS A CORTO PLAZO":
        print("PASIVOS A CORTO PLAZO")
        elret=2
    else:
        elret=404
    return elret

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
