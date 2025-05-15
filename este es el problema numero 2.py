def problema_2():
    print("PROBLEMA 2: Múltiplos de un número")
    numero = int(input("Ingrese un número positivo: "))
    if numero > 0:
        print("Los primeros 9 múltiplos de", numero, "son:")
        i = 1
        while i <= 9:
            print(numero * i)
            i = i + 1
    else:
        print("Solo se permiten números positivos.")

def menu():
    opcion = 0
    while opcion != 3:
        print("\n--- MENÚ DE OPCIONES ---")
        print("1. Problema 1")
        print("2. Problema 2")
        print("3. Salir")
        opcion = int(input("Elija una opción: "))

        if opcion == 1:
            problema_1()
        elif opcion == 2:
            problema_2()
        elif opcion == 3:
            print("Fin del programa.")
        else:
            print("Opción no válida.")
