import random
from os import system

def juego():
    numeros = [1, 2, 3, 4, 5, 6, 7, "sota", "caballo", "rey"]
    palos = ["Oro", "Basto", "Espadas", "Copas"]
    valores = [1,2,3,4,5,6,7,10,11,12]
    lista_cartas = []


    platilla_carta = {
        "numero": "",
        "palo": "",
        "valor": ""
    }

    lista_cartas = []
    for numero in numeros:
        for palo in palos:
            carta=platilla_carta.copy()
            carta["numero"]=numero
            carta["palo"]=palo
            for valor in valores:
                carta["valor"]=numero
                if carta["numero"]=="sota":
                    carta["valor"]=10
                elif carta["numero"] =="caballo":
                        carta["valor"] = 11
                elif carta["numero"] =="rey":
                            carta["valor"] = 12

            lista_cartas.append(carta)


    return  lista_cartas





def barajar():
    baraja = juego()
    cartas_barajadas=[]

    for carta in baraja:
        x=random.randint(0,len(cartas_barajadas))
        cartas_barajadas.insert(x,carta)
    return cartas_barajadas
#print(barajar())

def repartir(numero_jugadores,cartas_repartidas):
    montones = []
    baraja=barajar()

    if numero_jugadores*cartas_repartidas>len(baraja):
        return "No podemos jugar asi picha"


    for reparto in range (numero_jugadores):
        mazo_jugador=[]

        for cartas in range (cartas_repartidas):
            mazo_jugador.append(baraja[0])
            baraja.remove(baraja[0])
        montones.append(mazo_jugador)

    return montones
