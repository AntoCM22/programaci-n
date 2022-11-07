"""Ejercicio 1 - El calculador de mitades
Se desea realizar una función en python que reciba un número, y que devuelva la lista de las
posibles divisiones de ese número entre 2 , con división exacta, hasta llegar a 0 o hasta que
hasta que el número por el que vayamos no se pueda dividir entre 2. A continuación se
muestran varios ejemplos de ejecución."""



def division (numero):
    list=[]
    list.append(numero)
    if numero%2!=0:
        print("¡No puedo hacerlo crack!")
    else:

     while numero%2==0:
        list.append(int(numero/2))
        numero = int(numero/2)


    if list[-1]==1:
        print("Esto numero es potencia de 2")
    elif len(list)!=1:
        print("Esto he conseguido")




    return list


print(division(3))