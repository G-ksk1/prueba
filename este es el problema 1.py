
def problema_1():
    print("PROBLEMA 1: Ingresar 10 números positivos")
    numeros = []
    contador = 1

    while contador <= 10:
        num = int(input("Ingrese un número positivo: "))
        if num > 0:
            numeros.append(num)
            contador = contador + 1
        else:
            print("Solo se permiten números positivos.")

    digitos = 0
    decenas = 0
    centenas = 0

    for numero in numeros:
        if numero >= 0 and numero <= 9:
            digitos = digitos + 1
        elif numero >= 10 and numero <= 99:
            decenas = decenas + 1
        elif numero > 99:
            centenas = centenas + 1

    print("Cantidad de dígitos (0-9):", digitos)
    print("Cantidad de decenas (10-99):", decenas)
    print("Cantidad de centenas (>99):", centenas)
