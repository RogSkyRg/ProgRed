'''
Nombre: Méndez Fernandez Alan Eusebio
Descripcion: Lab 3.1.1.11
Fecha: 30/10/2024
'''

ingreso = float(input("Introduce el ingreso anual: "))

if ingreso <= 0:
    impuesto = 0.0
elif ingreso <= 85528:
    impuesto = (ingreso * 0.18) - 556.02
else:
    impuesto = 14839.02 + (ingreso - 85528) * 0.32

if impuesto < 0:
    impuesto = 0.0

impuesto = round(impuesto, 0)

print("El impuesto es:", impuesto, "pesos")