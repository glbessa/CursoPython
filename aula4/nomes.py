nomes = []

nome = input("Digite um nome: ")
while nome != "sair":
    nomes.append(nome)
    nome = input("Digite um nome: ")

for i, nome in enumerate(nomes):
    print(f"Indíce: {i} - Nome: {nome}")