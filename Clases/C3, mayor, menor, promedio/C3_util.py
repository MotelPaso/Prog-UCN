
#maximo
total = 10
for i in range(total):
    if i > maximo:
        maximo = i
    # minimo
    if i < minimo:
        minimo = i
    # promedio
    suma += i
    promedio = suma * 100 /total