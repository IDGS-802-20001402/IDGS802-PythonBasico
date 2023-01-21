num1 = int(input("Escriba el primer valor "))
num2 = int(input("Escriba el segundo valor "))

if num1 > num2:
    print("El numero {} es mayor que el {}".format(num1, num2))
else:
    print("El numero {1} es mayor que el {0}".format(num1, num2))


print('---------------Pedir una edad--------------------')
edad = int(input("Ingrese su edad "))

if edad > 18:
    print("Eres mayor de edad")
elif edad == 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")