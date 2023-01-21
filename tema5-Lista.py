# Listas
# * una lista es una secuencia de elementos
# *Cuando se asigna a una variable, permite agrupar varios elementos en un oslo lugar
# * Se crean con los [] o con la keywor list

lista1 = ["Cristian", 20, 10, True, "Ruiz", 21, 9]

print(lista1)
print(lista1[:])
print(lista1[2])
print(lista1[-2])
print(lista1[:3])
print(lista1[4:])

lista1.append("Ruiz")

print(lista1)

lista1.insert(2, "Prueba")

print(lista1)

lista1.extend(["uno", 1.1, False])
print(lista1)

lista1.remove(20)
print(lista1)

lista1.pop(0)
print(lista1)

lista2 = ["Hola", "Mundo"]
lista3 = lista1 + lista2
print(lista3)

print(lista2 * 4)

lista4 = [2,6,5,4,8]
lista4.sort()
print(lista4)


del lista4[0]
print(lista4)