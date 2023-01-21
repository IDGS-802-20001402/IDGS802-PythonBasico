num1 = 20
num2 = 0


try:
    print("La division de {} entre {} es {}".format(num1, num2, (num1/num2)))
except ZeroDivisionError:
    print("Ocurrio un error...")
finally:
    print("El programa se ha ejecutado")