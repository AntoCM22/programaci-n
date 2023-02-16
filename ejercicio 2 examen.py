




def ahorcado(jug):
    vidas = 5
    letras_citadas = []
    palabra_secreta = []
    palabra = input("¿Qué palabra quieres hacer que adivinen?")
    lista_palabra= list(palabra)
    palabra_secreta_vacia = True

    while vidas>0 or palabra_secreta_vacia == True:
        for letra in range(len(lista_palabra)):


            letra = input("¿Que letra vas a usar?")

            if letra in lista_palabra:
                tablero = ["_"] * len(lista_palabra)
                print("Acertaste")
                print(tablero)
                palabra_secreta.append(letra)
                print(palabra_secreta)
                print("Has usado estas letras:"+str(letras_citadas))
                print("Te quedan " + str(vidas) + " vidas")

                if palabra_secreta_vacia==len(lista_palabra):
                     palabra_secreta_vacia = False


            else:
                print("Fallaste")
                letras_citadas.append(letra)
                print("Has usado estas letras:"+str(letras_citadas))
                vidas-=1
                print("Te quedan " + str(vidas) + " vidas")
                if vidas == 0:
                    palabra_secreta_vacia == False

    else:
        print("Has perdido")


ahorcado(1)




