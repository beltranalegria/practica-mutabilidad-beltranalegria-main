def probar():
    a = (1, 2, [1, 2, 3])
    a[2].append(4)
    print(a)

probar()
# Explicación: En este caso, la posicion dos de la tupla a es la lista [1, 2, 3], que es mutable. 
# Al hacer append(4), se modifica la lista dentro de la tupla, pero la tupla en sí no cambia. 
# Por lo tanto, el resultado es (1, 2, [1, 2, 3, 4]), mostrando que la tupla contiene una lista modificada.


