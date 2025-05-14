def problema2():
    print("\n--- Problema 2 ---")
    try:
        numero = int(input("Ingrese un número positivo para ver sus múltiplos: "))
        if numero <= 0:
            print("Debe ser un número positivo.")
            return
        print(f"Los primeros 9 múltiplos de {numero} son:")
        for i in range(1, 10):
            print(numero * i, end=" ")
        print()
    except ValueError:
        print("Entrada inválida. Intente nuevamente.")


def menu():
    while True:
        print("\n--- Menú de Opciones ---")
        print("1. Resolver Problema 1")
        print("2. Resolver Problema 2")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            problema1()
        elif opcion == "2":
            problema2()
        elif opcion == "3":
            print("¡Gracias por usar el programa!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
