"""
Desafio 1:
Consiste en 
Encontrar cuantos numeros primos hay en un rango determinado
Imprimir algo basado en la suma de los primos
"""
ultimoprimo = 0
penprimo = 0
contador = 0
suma = 0

inicio = int(input("Inicio: "))
fin = int(input("Fin: "))

while inicio <= 1 or fin < inicio:
    print("Error")
    inicio = int(input("Inicio: "))
    fin = int(input("Fin: "))

print("Primos:")
for i in range(2, fin): # Revisamos numero a numero
    es_primo = 1
    for j in range(2, i):
        if i % j == 0:
            es_primo = 0
    if es_primo == 1 and i >= inicio:
        print(i)
        contador += 1
        suma += i

        if i > penprimo:
            if i > ultimoprimo:
                penprimo = ultimoprimo
                ultimoprimo = i

if contador >= 2:
    print(f"Los dos mayores son: {ultimoprimo} y {penprimo}")
else:
    print("No hay primos suficientes")

print(f"La suma es: {suma}")

if suma % 2 == 0 or suma % 3 == 0 or suma % 5 == 0:
    if suma % 2 == 0:
        print("Soy par")
    if suma % 3 == 0:
        print("Si")
    if suma % 5 == 0:
        print("Cinco")
else:
    print("No")
