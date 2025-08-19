def remover_elemento(cadena, elemento):
    return "".join(filter(lambda x: x != elemento, cadena))

texto = "banana"
resultado = remover_elemento(texto, "a")

print(resultado)
print(texto)      
print(texto is resultado)  # False (objetos distintos) y las cadenas son iterables
print(id(resultado), id(texto))            