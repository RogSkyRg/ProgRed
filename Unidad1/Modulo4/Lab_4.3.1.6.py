'''
Nombre: Mendez Fernandez Alan Eusebio
Descripcion: Lab 4.3.1.6
Fecha: 30/10/2024
'''

def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

test_data = [1900, 2001, 2016, 1987]
test_results = [False, True, True, False]

for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("True")
    else:
        print("False")