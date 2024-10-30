'''
Nombre: Méndez Fernandez Alan Eusebio
Descripcion: Lab 4.3.1.10
Fecha: 30/10/2024
'''

def liters_100km_to_miles_gallon(liters):
    miles_per_100km = 100 * 1000 / 1609.344
    gallons = liters / 3.785411784
    return miles_per_100km / gallons

def miles_gallon_to_liters_100km(miles):
    km_per_mile = 1609.344 / 1000
    liters_per_gallon = 3.785411784
    return liters_per_gallon / (miles * km_per_mile) * 100

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))