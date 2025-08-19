# Tu implementacion va aqui
def hola_mundo():
    return "hola_mundo"

def ejemplo_append():
    lista = [1, 2, 3]
    copia = lista
    lista.append(4)
    print("append:", lista, copia)  # ambas cambian → [1,2,3,4]b thet

def ejemplo_extend():
    lista = [1, 2]
    copia = lista
    lista.extend([3, 4, 5])
    print("extend:", lista, copia)  # [1,2,3,4,5]   

def ejemplo_insert():
    lista = ["a", "c"]
    copia = lista
    lista.insert(1, "b")
    print("insert:", lista, copia)  # ["a","b","c"]

def ejemplo_remove():
    lista = [10, 20, 30, 20]
    copia = lista
    lista.remove(20)
    print("remove:", lista, copia)  # [10,30,20] → solo borra la primera ocurrencia

def ejemplo_pop():
    lista = ["x", "y", "z"]
    copia = lista
    eliminado = lista.pop(1)
    print("pop:", lista, copia, "eliminado:", eliminado)  # ["x","z"], eliminado "y"


def main():
    ejemplo_append()
    ejemplo_extend()
    ejemplo_insert()
    ejemplo_remove()
    ejemplo_pop()

if __name__ == "__main__":
    main()