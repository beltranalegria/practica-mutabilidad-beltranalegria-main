profe= "Agostina"
mi_profe= "Agostina"
print(profe is mi_profe) # Completar en este comentario: ¿qué valor se obtuvo? True

pro= "Agostina?"
pro_Agos= "Agostina?"
print(pro is pro_Agos)  # Completar en este comentario: ¿qué valor se obtuvo? True 

a="a"
b="b"
print(a is b)  # Completar en este comentario: ¿qué valor se obtuvo? False

ver="!"
ver_mas="!"
print(ver is ver_mas)  # Completar en este comentario: ¿qué valor se obtuvo? True

numero1=120
numero2=120
print(numero1 is numero2)  # Completar en este comentario: ¿qué valor se obtuvo? True

numero1=12000000
numero2=12000000
print(numero1 is numero2)  # Completar en este comentario: ¿qué valor se obtuvo? False

lista1=[1,2,3,4]
lista2=[1,2,3,4]
print(lista1 is lista2) # Completar en este comentario: ¿qué valor se obtuvo? False

lista3=lista1
print(lista3 is lista1) # Completar en este comentario: ¿qué valor se obtuvo? True

lista4=lista1[:]
print(lista4 is lista1) # Completar en este comentario: ¿qué valor se obtuvo? False
print(id(lista3), id(lista1))
