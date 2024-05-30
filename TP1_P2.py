def obtener_datos(color, año):
    cantidad = int(input(f"Ingrese la cantidad de lapiceras {color} para el año {año}: "))
    precio_unitario = float(input(f"Ingrese el precio unitario de las lapiceras {color} para el año {año}: "))
    return {"cantidad": cantidad, "precio_unitario": precio_unitario}

lapiceras_2022 = {}
lapiceras_2023 = {}
for color in ["azules", "rojas", "verdes"]:
    lapiceras_2022[color] = obtener_datos(color, 2022)
    lapiceras_2023[color] = obtener_datos(color, 2023)

costo_2022 = sum(lapiceras_2022[color]["cantidad"] * lapiceras_2022[color]["precio_unitario"] for color in lapiceras_2022)
costo_2023 = sum(lapiceras_2023[color]["cantidad"] * lapiceras_2023[color]["precio_unitario"] for color in lapiceras_2023)

stock = {color: lapiceras_2022[color]["cantidad"] + lapiceras_2023[color]["cantidad"] for color in lapiceras_2022}

print(f"\nCosto de compra en 2022: ${costo_2022:.2f}")
print(f"Costo de compra en 2023: ${costo_2023:.2f}")
print("Stock de lapiceras por color:")
for color in stock:
    print(f"  {color.capitalize()}: {stock[color]} unidades")