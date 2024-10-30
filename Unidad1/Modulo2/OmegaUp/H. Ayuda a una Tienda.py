def calcular_pago(monto):
    if monto < 500:
        descuento = 0
    elif 500 <= monto <= 1000:
        descuento = 0.05
    elif 1001 <= monto <= 7000:
        descuento = 0.11
    elif 7001 <= monto <= 15000:
        descuento = 0.18
    else:
        descuento = 0.25
    
    monto_final = monto * (1 - descuento)
    return monto_final

compras = list(map(float, input().split()))

for compra in compras:
    monto_a_pagar = calcular_pago(compra)
    print(f"{monto_a_pagar:.2f}")
