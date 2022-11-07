from ast import Delete
from baraja_main import *



def veintiuno(num_jugadores):

    suma_mazo=0
    mazo1=[]
    banderamazo1 = True
    mazo2=[]
    banderamazo2= True
    mazo3=[]
    banderamazo3= True
    mazo4=[]
    banderamazo4= True
    cartas_jugadores = []
    suma_ganadora=21
#repartir entre jugadores
    if num_jugadores != 2 and num_jugadores != 4 and num_jugadores != 5 and num_jugadores != 8:
        print("No se puede jugar con estos jugadores picha , solo pueden jugar: 2-4-5 y 8")
    else:
        num_cartas_jugador=int(len(barajar())/num_jugadores)
        cartas_jugadores= repartir(num_jugadores,num_cartas_jugador)
        puntuaciones_jugadores=[]
        print (cartas_jugadores)
        for jugador in range(num_jugadores):
            
            puntuaciones_jugadores.append(0)

        jugador= 0

#Empieza el bucle del juego

        while banderamazo1==True or banderamazo2==True  or banderamazo3==True  or banderamazo4==True:
            print ("Puntuaciones: ", puntuaciones_jugadores)
            print ("Mazo 1:", mazo1)
            print ("Mazo 2:", mazo2)
            print ("Mazo 3:", mazo3)
            print ("Mazo 4:", mazo4)


#Iniciamos la variable en el caso que superemos el num de jugadores
           
            if jugador == num_jugadores:
                jugador= 0


#Le preguntamos al jugador que quiere hacer
            
            print("Jugador "+str(jugador+1)+", tu turno churrita!")
            if jugador == (num_jugadores-1):
                print (cartas_jugadores[-1])
            else:
                print (cartas_jugadores[jugador])
            pregunta=int(input("¿Que carta quieres meter?"))
            pregunta_mazo=int(input("¿A que mazo?"))
                    
                
            if pregunta_mazo==1 and banderamazo1:
                    mazo1.append(cartas_jugadores[jugador][pregunta-1])     
                    cartas_jugadores[jugador].pop(pregunta - 1)
                    suma_mazo=0 
                    for carta in range(len(mazo1)):         #Aqui meteremos las cartas de cada jugador en su determinado mazo.
                        suma_mazo += mazo1[carta]["valor"]
                    if suma_mazo == suma_ganadora:
                        print("Eso es un puntito , buena")
                        puntuaciones_jugadores[jugador]= puntuaciones_jugadores[jugador] +1
                        banderamazo1 = False
                    elif suma_mazo > suma_ganadora:
                        banderamazo1 = False
                    
            
            elif pregunta_mazo==2 and banderamazo2:
                    mazo2.append(cartas_jugadores[jugador][pregunta-1])
                    cartas_jugadores[jugador].pop(pregunta - 1)
                    suma_mazo2=0
                    for carta in range(len(mazo2)):
                        suma_mazo2 += mazo2[carta]["valor"]
                    if suma_mazo2 == suma_ganadora:
                        print("Eso es un puntito , buena")
                        puntuaciones_jugadores[jugador]= puntuaciones_jugadores[jugador] +1
                        banderamazo2 = False
                    elif suma_mazo2 > suma_ganadora:
                        banderamazo2 = False
                    
                    
            elif pregunta_mazo==3 and banderamazo3:
                    mazo3.append(cartas_jugadores[jugador][pregunta-1])
                    cartas_jugadores[jugador].pop(pregunta - 1)
                    suma_mazo3=0
                    for carta in range(len(mazo3)):
                        suma_mazo3 += mazo3[carta]["valor"]
                    if suma_mazo3 == suma_ganadora:
                        print("Eso es un puntito , buena")
                        puntuaciones_jugadores[jugador]= puntuaciones_jugadores[jugador] +1
                        banderamazo3 = False
                    elif suma_mazo3 > suma_ganadora:
                        banderamazo3 = False
                    
                
            elif pregunta_mazo==4 and banderamazo4:
                    mazo4.append(cartas_jugadores[jugador][pregunta-1])
                    cartas_jugadores[jugador].pop(pregunta - 1)
                    suma_mazo4=0
                    for carta in range(len(mazo4)):
                        suma_mazo4 += mazo4[carta]["valor"]
                    if suma_mazo4 == suma_ganadora:
                        print("Eso es un puntito , buena")
                        puntuaciones_jugadores[jugador]= puntuaciones_jugadores[jugador] +1
                        banderamazo4 = False
                    elif suma_mazo4 > suma_ganadora:
                        banderamazo4 = False
                    
            else:
                    print("Ese mazo ya ha sido completado, pasa al siguiente por no prestar atención churra")

            jugador +=1
#Aqui finaliza la introduccion de cartas a los mazos de encima de la mesa.

        numero_ganador=0
        for puntuacion in range(puntuaciones_jugadores):                #Para determinar el ganador o ganadores del juego
            if puntuaciones_jugadores(puntuacion)>numero_ganador:
                numero_ganador=puntuaciones_jugadores(puntuacion)


        for puntuacion in range(puntuaciones_jugadores):
            if puntuaciones_jugadores(puntuacion)==numero_ganador:
                print ("Jugador "+ str (puntuacion + 1) + " es ganador") 
                    
                 
            
            
                

veintiuno(2)




















