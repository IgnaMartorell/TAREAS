def obtener_datos(producto):
    cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
    precio_unitario = float(input(f"Ingrese el precio unitario de {producto}: "))
    return cantidad, precio_unitario

def calcular_gasto():
    cantidad_coca_cola, precio_unitario_coca_cola = obtener_datos("Coca Cola")
    cantidad_pepsi, precio_unitario_pepsi = obtener_datos("Pepsi")
    cantidad_mirinda, precio_unitario_mirinda = obtener_datos("Mirinda")
    cantidad_fanta, precio_unitario_fanta = obtener_datos("Fanta")

    costo_coca_cola = cantidad_coca_cola * precio_unitario_coca_cola
    costo_pepsi = cantidad_pepsi * precio_unitario_pepsi
    costo_mirinda = cantidad_mirinda * precio_unitario_mirinda
    costo_fanta = cantidad_fanta * precio_unitario_fanta

    gasto_estimado = costo_coca_cola + costo_pepsi + costo_mirinda + costo_fanta

    impuesto = 0.21 * gasto_estimado

    gasto_final = gasto_estimado + impuesto

    print(f"El gasto total incluyendo el impuesto es: ${gasto_final:.2f}")

calcular_gasto()