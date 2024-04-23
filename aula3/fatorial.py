n1 = int(input("Fatorial de: "))
acumulador = 1

for i in range(1, n1 + 1):
    acumulador = acumulador * i

i = n1
while i > 0:
    acumulador = acumulador * i
    i -= 1

print(f"{n1}! = {acumulador}")