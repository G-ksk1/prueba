def problema1():
    numeros = []
    print("\n--- Problema 1 ---")
    while len(numeros) < 10:
        try:
            num = int(input(f"Ingrese el número entero positivo #{len(numeros)+1}: "))
            if num > 0:
                numeros.append(num)
            else:
                print("Debe ser un número positivo.")
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

    digitos = sum(1 for n in numeros if 0 <= n <= 9)
    decenas = sum(1 for n in numeros if 10 <= n <= 99)
    centenas = sum(1 for n in numeros if n >= 100)

    print(f"\nResultados:")
    print(f"Cantidad de dígitos (0-9): {digitos}")
    print(f"Cantidad de decenas (10-99): {decenas}")
    print(f"Cantidad de centenas (>99): {centenas}")
