x = int(input("Ingresa un número: "))
r = x%2

if x % 2 == 0:
    msj = "par "
else:
    msj = "impar "

print("El numero " + str(x) + " es " + msj)
