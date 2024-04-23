frutas = ["maça", "banana", "uva", "pessego"]
frutas_vermelhas = ["amora", "framboesa", "morango", "mirtilo"]

# remover itens
primeira_fruta = frutas.pop(0)

# inserir itens
frutas.append("laranja")
frutas.insert(0, "abacate")

# juntas listas
frutas.extend(frutas_vermelhas)

# inverter lista
frutas = frutas[::-1]
primeira_parte = frutas[0:3]
segunda_parte = frutas[3:7:2]
frutas.reverse()

# ordenar
frutas.sort()

print(primeira_fruta)

print(primeira_parte)
print(segunda_parte)

print(frutas)
print(len(frutas))

frutas2 = frutas.copy()

frutas[8] = 'bergamota'

#print(dir(frutas2))

# remover
frutas.remove('bergamota')

for i, fruta in enumerate(frutas):
    print(f"Indíce: {i} - Fruta: {fruta}")