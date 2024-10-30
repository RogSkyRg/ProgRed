def hay_interseccion(a, b, c, d):
    if max(a, c) <= min(b, d):
        return 1
    else:
        return 0

a, b, c, d = map(int, input().split())

print(hay_interseccion(a, b, c, d))
