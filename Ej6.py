def remover_elemento(lista, elemento):
    return list(filter(lambda x: x != elemento, lista))

frutas = ["banana", "pera", "mandarina"]
frutas_amarillas = remover_elemento(frutas, "mandarina")


print(frutas_amarillas)          # ['banana', 'pera']
print(frutas)                    # ['banana', 'pera', 'mandarina']
print(frutas_amarillas is frutas) # False (objetos distintos)
print(id(frutas_amarillas), id(frutas))  # ids diferentes