#PROBLEMA 3
#Se desea calcular el sueldo de los siguientes empleados:
# Martinez tiene un sueldo de $30.000.-
# Juarez tiene un sueldo de $40.000.-
# Mendoza tiene un sueldo de $55.000.-
#Se pide tener un total de sueldos a pagar y sobre ese total calcular el 3% de obra social y
#14% de jubilación. Dichos porcentajes se descuentan del sueldo ya que se debe enviar a
#los organismos controladores. Por lo tanto se desea saber cuánto realmente se debe
#disponer para pagarle a los empleados.



# Solicitar al usuario que ingrese los sueldos de cada empleado
sueldo_martinez = float(input("Ingrese el sueldo de Martinez: "))
sueldo_juarez = float(input("Ingrese el sueldo de Juarez: "))
sueldo_mendoza = float(input("Ingrese el sueldo de Mendoza: "))

# Calculo del total de sueldos a pagar
total_sueldos = sueldo_martinez + sueldo_juarez + sueldo_mendoza

# Calculo del descuento por obra social y jubilación
descuento_obra_social = total_sueldos * 0.03
descuento_jubilacion = total_sueldos * 0.14

# Total a disponer para pagarle a los empleados
total_a_disponer = total_sueldos - descuento_obra_social - descuento_jubilacion

# Impresión de los resultados
print("Total de sueldos a pagar:", total_sueldos)
print("Descuento por obra social:", descuento_obra_social)
print("Descuento por jubilación:", descuento_jubilacion)
print("Total a disponer para pagar a los empleados:", total_a_disponer)