num1 = 15
num2 = 4

print("Suma: ", (num1 + num2))
print("Resta: ", (num1 - num2))
print("Multiplicacion", (num1 * num2))
print("Division: ", (num1 / num2))
print("Division Exacta: ", (num1 // num2))
print("Potencia: ", (num1 ** num2))

# concatenacion en python
texto1 = "Hola"
texto2 = "Mundo"
textoFinal = texto1 + " " + texto2

print(textoFinal)
print("El saludo es: %s %s" %(texto1, texto2))

saludoFinal = "Saludo: {1} {0}".format(texto1, texto2)
print(saludoFinal)

saludoFinal2 = "Saludo 2: {y} {x}".format(x=texto1, y=texto2)