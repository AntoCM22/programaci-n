"EJERCICIO 3 : Responde si o no y te dara posibles resultados"



def ropa ():
    resp1 = input("¿Hace frio?")
    while resp1!='si'and resp1!='no':
        resp1 = input("¿Hace frio?")
    resp2 = input("¿Hace sol?")
    while resp2 != 'si' and resp2!= 'no':
            resp2 = input("¿Hace sol?")
    resp3 = input("¿Está lloviendo?")
    while resp3 != 'si' and resp3 != 'no':
        resp3 = input("¿Está lloviendo?")

    if resp1 == 'si' and resp2 == 'si':
        print("nada socio , una cazadora rechulona")


    elif resp1=='no'and resp2=='si' and resp3=='no':
            print("Gorra socio  y sin abrigo que hace calor")
    elif resp1=='si' and resp2=='no' and resp3=='no':
            print("nada socio , un chaquetoncito")
    elif resp1=='si' and resp2 =='no' and resp3=='si':
        print("Gorrito de lluvia, socio y chubasquero , que no cale")
    elif resp1=='no' and resp2=='no' and resp3=='no':
        print("Gorra , socio y una chaquetita niño")
    elif resp1=='no' and resp2=='no' and resp3=='si':
        print("Gorrito de lluvia, socio")

ropa()