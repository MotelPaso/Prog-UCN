
"""
Created on Sat Apr 12 18:53:08 2025
"""
def entre(primero, segundo, a):
    if a == "suma":
        respuesta = 0
        for i in range(primero,segundo+1):
            respuesta += i
    if a == "multiplicacion":
        respuesta = 1
        for i in range(primero,segundo+1):
            respuesta *= i

    return respuesta

num1 = int(input("Ingrese su primer numero: "))
num2 = int(input("Ingrese su segundo numero: "))

print("Posibles Operaciones:")
print("Suma: +")
print("Mult: x")
operacion = input("Seleccione su operacion:")

while operacion != "suma" and operacion != "multiplicacion":
    print("Operacion no es valida.")
    operacion = input("Seleccione su operacion:")
print(operacion)

print(entre(num1,num2,operacion))