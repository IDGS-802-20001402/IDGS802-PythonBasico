num = int(input("Escriba un valor "))
rango = range(1, 11)

for index in rango:
    print("{} x {} = {}".format(num, index, (num * index)))