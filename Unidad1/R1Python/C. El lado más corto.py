import math

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
x3, y3 = map(float, input().split())
x4, y4 = map(float, input().split())

lado1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
lado2 = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
lado3 = math.sqrt((x4 - x3)**2 + (y4 - y3)**2)
lado4 = math.sqrt((x1 - x4)**2 + (y1 - y4)**2)

lado_mas_corto = min(lado1, lado2, lado3, lado4)

print(lado_mas_corto)
