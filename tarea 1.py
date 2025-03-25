num1=0; #definición de la variable numero 1
num2=0; #definición de la variable numero 2
num3=0; #definición de la variable numero 3

num1=int(input("Ingrese un número entero: ")) #captura los datos
num2=int(input("Ingrese otro número entero: "))
num3=int(input("Ingrese de nuevo otro número entero: "))

if num1 > num2 and num1 > num3: #indica si el primer numero es mayor al segundo y el tercero
    mayor = num1
    print("El primer numero es mayor.") #Si es mayor, se mostrara un mensaje indicandolo
else:
    print("El primer número no es el mayor.") #Si no es así, mostrara el mensaje contrario

if num2 > num1 and num2 > num3: #indica si el segundo numero es mayor al primero y el tercero
    mayor = num2
    print("El segundo numero es mayor.") #Si es mayor, se mostrara un mensaje indicandolo
else:
    print("El segundo número no es el mayor.") #Si no es así, mostrara el mensaje contrario

if num3 > num1 and num3 > num2: #indica si el tercer numero es mayor al primero y el segundo
    mayor = num3
    print("El tercer numero es mayor.") #Si es mayor, se mostrara un mensaje indicandolo
else:
    print("El tercer número no es el mayor.") #Si no es así, mostrara el mensaje contrario
