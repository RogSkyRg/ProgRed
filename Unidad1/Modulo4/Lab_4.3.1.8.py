'''
Nombre: Méndez Fernandez Alan Eusebio
Descripcion: Lab 4.3.1.8
Fecha: 30/10/2024
'''

def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month < 1 or month > 12:
        return None
    if year < 0:
        return None
    if month == 2 and is_year_leap(year):
        return 29
    else:
        return month_days[month - 1]

def day_of_year(year, month, day):
    if month < 1 or month > 12 or day < 1 or day > days_in_month(year, month):
        return None
    
    total_days = 0
    for m in range(1, month):
        total_days += days_in_month(year, m)
    total_days += day
    
    return total_days

print(day_of_year(2000, 12, 31))  
print(day_of_year(2023, 10, 3))  