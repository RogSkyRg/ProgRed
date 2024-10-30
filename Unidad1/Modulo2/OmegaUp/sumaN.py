

data = input("")
N = data.split()
N = str(data)
suma = sum(int(digit) for digit in N if digit.isdigit())
print(suma)
