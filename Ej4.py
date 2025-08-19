def reemplazar (cad , i , c):
    if i>=len(cad) or i<0:
        return cad , print("Índice fuera de rango")
    for j in range(len(cad)):
        if j==i:
            cad = cad[:j] + c + cad[j+1:]
    return cad

original = "casado"
modificado = reemplazar(original, 2, "z")
print(modificado) # cazado
