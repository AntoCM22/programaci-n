import random
from os import system
import time


from random import randint


def juego():
    numeros = [1, 2, 3, 4, 5, 6, 7, "sota", "caballo", "rey"]
    palos = ["Oro", "Basto", "Espadas", "Copas"]
    valores = [1,2,3,4,5,6,7,0.5,0.5,0.5]
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
                if carta["valor"] in numeros[-3:]:
                    carta["valor"] = 0.5

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
        print(mazo_jugador)
        montones.append(mazo_jugador)

    return montones

#print(repartir(2,1))



def sieteYmedio(numero_jugadores):

    cartas_jugador=[]
    baraja_mezclada=barajar()
    puntuaciones_jugadores=[]
    jugador_ganador="ninguno"


    for jug in range(numero_jugadores):
        respuesta = input("¿Quieres cartita?")
        puntuacion_jugador = 0.0
        while respuesta=="si":
            carta_ronda = baraja_mezclada[-1]
            cartas_jugador.append(carta_ronda)
            baraja_mezclada.pop()
            print("Jugador "+str(jug+1))
            print('Mi mano:' + str(carta_ronda))
            puntuacion_jugador+=carta_ronda["valor"]
            print('tengo ' + str(puntuacion_jugador)+' puntos')
            respuesta = input("¿Quieres cartita?")

        else:
            print("Te has cagado eh...")
            time.sleep(2)
            system("cls")
        puntuaciones_jugadores.append(puntuacion_jugador)

    print(puntuaciones_jugadores)
    for i in range(numero_jugadores):
        puntuaciones_jugadores[i]-=7.5
        lista_absoluta=list(map(lambda i: abs(i),puntuaciones_jugadores ))






    print(lista_absoluta)
    ganador = []
    for x in range(0,len(lista_absoluta)):
        if lista_absoluta[x]== min(lista_absoluta):
            ganador.append(x)
    print(ganador)

    if len(ganador) <= 1:
        felipe = ganador[0]
        print("Ha ganado el jugador " + str(felipe + 1))

    else:
        print("Hay empate.")
        for felipe in range(0,len(ganador)):
            print("Han ganado los jugadores " + str(felipe + 1))









sieteYmedio(2)











