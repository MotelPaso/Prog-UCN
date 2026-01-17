"""
Ejercicio 4

Paulo César Araya Rojo
"""


arch = open("consumo.txt", "r", encoding = "utf-8")
arch2 = open("limites.txt", "r", encoding ="utf-8")

linea = arch.readline().strip()
# Variables creadas
sumatotal = 0 # Suma de todas las comunas
maximo = 0
minimo = 9999999 # max y min solicitados
maximo2 = 0
minimo2 = 9999999 # max y min de todas las comunas
pasaste = 0 # contador
contadortotal = 0 # contador de cuantas comunas
# tambien se podria hacer contando manualmente en el archivo

solicitada = input("Ingrese la comuna: ") # Ingresamos la comuna solicitada por el usuario

comunas = "Ñuñoa", "La Reina", "Maipú","Providencia","Puente Alto","Las Condes","San Bernardo","Recoleta","Renca","Pudahuel"

# Hacemos una variable con todas las comunas
# imporante que no cuenta como lista porque no tiene los []

while solicitada not in comunas:
    solicitada = input("Comuna no valida, Ingrese otra: ") # Si pide una comuna que existe

while linea != "":

    suma = 0 # Suma por comuna

    partes = linea.split(",") # Dividimos por linea
    comuna = partes[0] 
    cantMedi = int(partes[1])

    for i in range(cantMedi):
        suma += int(partes[i+2])
        promedio = suma / (cantMedi)

    sumatotal += suma

    linea2 = arch2.readline().strip() # Leemos el limite de la comuna
    partes2 = linea2.split(",") # Dividimos la linea
    # No es necesario revisar si las comunas son iguales entre archivos
    # Porque estan ordenados igual
    limite = int(partes2[1])
    
    if promedio <= limite:
        Estado = "EFICIENTE"
    if promedio > limite:
        Estado = "EXCESIVO"
        pasaste += 1 # Contador de estados excesivos
    
    if promedio > maximo2: # Maximo de la comuna
        maximo2 = promedio
        comunaMax = comuna

    if promedio < minimo2: # Minimo de la comuna
        minimo2 = promedio
        comunaMin = comuna

    if comuna == solicitada: # Aqui mostramos la comuna solicitada por el usuario
        print("-------------------------")
        print("Comuna", solicitada,"encontrada!")
        sumasoli = suma
        for i in range(cantMedi): # maximo
            if int(partes[i+2]) > maximo:
                maximo = int(partes[i+2])
            if int(partes[i+2])< minimo:
                minimo = int(partes[i+2])
        print("El promedio de consumo en la comuna es:",round(promedio,2))
        print("El consumo maximo en la comuna es de:",maximo)
        print("El consumo minimo en la comuna es de:",minimo)
        print("El estado en la comuna es:", Estado)
        print("-------------------------") # aqui conte los guiones de la prueba pero no hacia falta
    else: # Si la comuna no es la solicitada:
        print("Comuna:",comuna,"|","Promedio:",round(promedio,2),"| Estado:", Estado)
    contadortotal += 1

    linea = arch.readline().strip()
# Imprimimos todo basado en el ejemplo de salida
print("2)")
print("Comuna con mayor consumo promedio:", comunaMax, "con", maximo2, "de consumo promedio")
print("Comuna con mayor consumo promedio:", comunaMin, "con", minimo2, "de consumo promedio")
percent = pasaste*100/contadortotal
print("El porcentaje de comunas que superaron el limite es de:", percent,"%")
print("Consumo de:", solicitada, sumasoli,"kWh")
print("Consumo total acumulado de toas las comunas:", sumatotal,"kWh")
porcentaje = round(sumasoli*100/sumatotal,2)
print("La comuna de", solicitada, "representa el", porcentaje, "del consumo total de la ciudad")

