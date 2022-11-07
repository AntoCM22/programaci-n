"Ejercicio 2 - Carrito compra super"

def carrito(productos,cantidad, precio):

    if len(productos)==len(cantidad)==len(precio) and len(productos)>0:
        print("----RESUMEN DE TU COMPRA----")
        total=0
        for i in range(len(productos)):
            total+=(cantidad[i])*(precio[i])
            print(f'{productos[i]}---{cantidad[i]} Articulos-----{precio[i]}€')
        print('total------------------'+str(total)+ '€')
    else:
        print("No puedo hacer esta compra")

carrito(["doritos","figura pokemon"],[2,1],[3.5,7.2])
