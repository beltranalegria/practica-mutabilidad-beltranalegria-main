# Ejemplos de números complejos en Python

# Ejemplo 1: usando literales
c1 = 3 + 4j

# Ejemplo 2: solo parte imaginaria
c2 = 5j

# Ejemplo 3: usando la función complex()
c3 = complex(2, -3)

print("Ejemplo 1:", c1)  # (3+4j)
print("Ejemplo 2:", c2)  # 5j
print("Ejemplo 3:", c3)  # (2-3j)

# Demostración de que los números complejos son inmutables
c = 1 + 2j
c_copy = c
c += 3  # crea un nuevo objeto, suma 3 a la parte real
print("\nDemostración de inmutabilidad:")
print("c después de modificar:", c)         # (4+2j)
print("c_copy (original):", c_copy)         # (1+2j) → no cambió
