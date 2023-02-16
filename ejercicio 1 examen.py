def ejercicio1(texto):

    comas=","
    interrogaciones="?"
    puntos="."
    dos_puntos=":"
    num_comas = 0
    num_interrogaciones = 0
    num_puntos = 0
    num_dos_puntos = 0

    for letra in texto:
        if letra == comas:
            num_comas += 1
        elif letra == interrogaciones:
            num_interrogaciones+=1
        elif letra == puntos:
            num_puntos+=1
        elif letra == dos_puntos:
            num_dos_puntos += 1



    print("Signos de puntuacion encontrados:")
    print(str(num_comas) + (" Estas son las comas que hay"))
    print(str(num_interrogaciones) + (" Estas son las interrogaciones que hay"))
    print(str(num_puntos) + (" Estos son los puntos que hay"))
    print(str(num_puntos) + (" Estos son los dos puntos que hay"))




ejercicio1("yo me , llamo , antonio, adios ? ¿ ,")