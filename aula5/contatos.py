nomes = []
telefones = []

def inserir():
    nome = input("nome da pessoa: ")
    telefone = input("telefone da pessoa: ")
    nomes.append(nome)
    telefones.append(telefone)

def listar() -> None:
    for indice in range(len(nomes)):
        print(f"nome: {nomes[indice]} - telefone: {telefones[indice]}")

def listar2():
    for nome, telefone in zip(nomes, telefones):
        print(f"nome: {nome} - telefone: {telefone}")

def remover():
    nome = input("nome para remover: ")
    indice = nomes.index(nome)
    nomes.pop(indice)
    telefones.pop(indice)

def remover2(nome_para_remover: str):
    indice = nomes.index(nome_para_remover)
    nomes.pop(indice)
    telefones.pop(indice)

def sair():
    exit()

while True:
    comando = input("Comando: ")
    if comando == "sair":
        sair()
    elif comando == "adicionar":
        inserir()
    elif comando == "listar":
        listar()
    elif comando == "remover":
        remover()
    else:
        print("Comando não reconhecido!")
