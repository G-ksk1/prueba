def problema_1():
    numeros = []
    print("Ingrese 10 números enteros positivos:")
    while len(numeros) < 10:
        try:
            num = int(input(f"Número {len(numeros)+1}: "))
            if num > 0:
                numeros.append(num)
            else:
                print("Debe ser positivo.")
        except:
            print("Entrada no válida.")

    digitos = sum(1 for n in numeros if n <= 9)
    decenas = sum(1 for n in numeros if 10 <= n <= 99)
    centenas = sum(1 for n in numeros if n >= 100)

    print(f"\nCantidad de dígitos (0-9): {digitos}")
    print(f"Cantidad de decenas (10-99): {decenas}")
    print(f"Cantidad de centenas (>99): {centenas}")
