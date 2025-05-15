def problema_2():
    try:
        numero = int(input("Ingrese un número positivo: "))
        if numero > 0:
            multiplos = [numero * i for i in range(1, 10)]
            print(f"Los múltiplos de {numero} son: {multiplos}")
        else:
            print("Debe ingresar un número positivo.")
    except:
        print("Entrada no válida.")

def menu():
    while True:
        print("\n--- MENÚ DE OPCIONES ---")
        print("1. Problema 1 - Clasificación de números")
        print("2. Problema 2 - Múltiplos de un número")
        print("3. Salir")

        opcion = input("Seleccione una opción (1-3): ")

        if opcion == "1":
            problema_1()
        elif opcion == "2":
            problema_2()
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida.")

