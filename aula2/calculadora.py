# Requisita um número ao usuário
n1 = float(input("Digite um número: "))

# Requisita outro número ao usuário
n2 = float(input("Digite outro número: "))

# Requisita a operação ao usuário
op = input("Digite a operação (+, -, *, /, ^): ")

if op == "+":
    print(f"{n1} + {n2} = {n1 + n2}")
elif op == "-":
    print(f"{n1} - {n2} = {n1 - n2}")
elif op == "*":
    print(f"{n1} * {n2} = {n1 * n2}")
elif op == "/":
    print(f"{n1} / {n2} = {n1 / n2}")
elif op == "^":
    print(f"{n1} ^ {n2} = {n1 ** n2}")
else:
    print("Operação inválida!")