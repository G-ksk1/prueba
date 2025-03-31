def calcular_horas_extras():
    # Solicitar el nombre y las horas extras
    nombre = input("Ingrese el nombre del empleado: ")
    horas_extras = int(input("Ingrese las horas extras trabajadas: "))
    
    # Calcular el total de horas según las horas extras
    if horas_extras > 75:
        pago_por_hora_extra = 75
    elif horas_extras > 50:
        pago_por_hora_extra = 65
    elif horas_extras > 25:
        pago_por_hora_extra = 50
    else:
        pago_por_hora_extra = 0  # Si no se supera las 25 horas extras, no hay pago
    
    total_pago = horas_extras * pago_por_hora_extra
    total_horas = horas_extras + 40  # Considerando que la jornada laboral estándar es de 40 horas
    
    # Mostrar los resultados
    print(f"Empleado: {nombre}")
    print(f"Total de horas trabajadas (incluyendo horas extras): {total_horas}")
    print(f"Total a pagar por horas extras: Q{total_pago:.2f}")
    
# Llamada a la función
calcular_horas_extras()
