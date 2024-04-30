contatos = {}
#contatos = dict()

def adicionar(contatos, nome, telefone):
    contatos.update(
        { nome: telefone }
    )

adicionar(contatos, "Gabriel", "123")

print(contatos)

nome_procurar = input("Nome para procurar: ")

#print(contatos["Pedro"])
#print(contatos.get("Pedro"))

resultado = contatos.get(nome_procurar)
if resultado != None:
    print(resultado)
else:
    print("Nome não existe!")

contatos.update(
    {
        "Pedro": "345"
    }
)

print(contatos)

print(contatos.items())