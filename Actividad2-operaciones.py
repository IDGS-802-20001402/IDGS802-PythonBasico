import os


class OperacionesBasicas:

    a = 0
    b = 0

    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2
        pass

    def suma(self):
        print('La suma es {}'.format(self.a+self.b))

    def resta(self):
        print('La resta es {}'.format(self.a-self.b))

    def multiplicacion(self):
        print('La multiplicacion es {}'.format(self.a*self.b))

    def division(self):
        print('La division es {}'.format(self.a/self.b))


def main():

    seleccion = 0
    
    while (seleccion != 5):

        os.system('cls')
        print("Seleccione una operacion: 1.Sumar \n 2.Restar \n 3.Multiplicar \n 4.Dividir \n 5.Salir")
        seleccion == int(input("Escriba una opción "))

        numa = int(input("Escriba el primer valor "))
        numb = int(input("Escriba el segundo valor "))

        obj = OperacionesBasicas(numa, numb)

        if (seleccion == 1):
            obj.suma()
        elif (seleccion == 2):
            obj.resta()
        elif (seleccion == 3):
            obj.multiplicacion()
        elif (seleccion == 4):
            obj.division()

if __name__ == "__main__":
    main()
    # Declaracion de metodos de clase
