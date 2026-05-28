import random
try:
    print("--------------------------------------------------------")
    print("------------JUGAREMOS AL JUEGO DEL PAR/IMPAR------------")
    print("--------------------------------------------------------")

    condicion = True
    while condicion == True:
        minimo = int(input("Ingresa un número: "))
        maximo = int(input("Ingresa un número (mayor al anterior): "))
        if maximo <= minimo:
            print("El segundo número NO es mayor al primero")
        else:
            condicion = False
    
    print("Respecto al rango que TÚ nos diste, saldrá un número aleatorio y nos tienes que decir si es par o impar")
    print("Por cada buena añades 100 puntos a tu carrito, donde los podrás canjear por productos que cuestan 1000 c/uno")
    cantidad = int(input("¿Cuántas veces te gustaría jugar? "))
    listo = input("presiona ENTER cuando estés listo ")

    puntos = 0
    for i in range(cantidad):
        aleatorio = random.randint(minimo,maximo)
        print(f"El número es: {aleatorio}")
        if aleatorio % 2 == 0:
            aleatorio = "par"
        else:
            aleatorio = "impar"
        respuesta = input("¿Par o impar? ").lower()
        if respuesta == aleatorio:
            print("¡Excelente!")
            puntos = puntos +150
        else:
            print("¡Error!")

    menu = True
    while menu == True:
        print("Ahora puedes hacer lo siguiente...")
        print("1.- Mostrar cantidad de puntos")
        print("2.- Canejar tus puntos en la tienda")
        print("3.- Salir")
        opcion = int(input("¿Que deseas hacer? (1,2 o 3) "))
        if opcion == 1:
            print(f"Tienes en total de {puntos} puntos")
        elif opcion == 2:
            comprar = input("¿Qué deseas comprar? puede ser una pelota, un peluche o un auto de juguete (coste de 1000 puntos) ")
            if puntos >= 1000:
                puntos = puntos - 1000
                print(f"Ahora te quedan {puntos} puntos")
            else:
                print("No tienes los puntos necesarios")
        elif opcion == 3:
            print("¡Nos vemos!")
            menu = False
except ValueError:
    print("Error en el ingreso de datos")