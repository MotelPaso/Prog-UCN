
a = int(input("Ingrese su numero aqui!"))
b = int(input("ingrese el otro numero"))

if b == 0:
    print(f"No se puede dividir por {b}")
elif a % b == 0:
    division = a//b
    print(f'Es entera y es igual a {division}')
else:
    print('Division no entera.')

if a == b:
    print("Son iguales")
elif a > b:
    print(f"{a} es mayor a {b}")
else:
    print(f"{b} es mayor a {a}")


