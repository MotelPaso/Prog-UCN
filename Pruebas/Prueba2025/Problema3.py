"""
Ejercicio 3

Paulo César Araya Rojo
"""
def partes(a): # Funcion para hacer partes = linea.split(',')
    partes = a.split(",")
    fecha = partes[0]
    hora = partes[1]
    preciototal = partes[2]
    cantProductos = int(partes[3])
    return fecha, hora, preciototal, cantProductos
# No es necesaria pero pense que entraban funciones

def dividir(b): # lo mismo
    dividir = b.split(",")
    item = dividir[0]
    precio = int(dividir[1])
    return item, precio
# Hay que tener cuidado que variables van dentro del while
montoCafe = 0
montoEmp = 0
montoChap = 0
montoSand = 0
montoAgua = 0
montoGall = 0
montoBeb = 0
montoMuff = 0

contCafe = 0
contEmp = 0
contChap = 0
contSand = 0
contAgua = 0
contGall = 0
contMuff = 0
contBeb = 0

totalProductos = 0
# Todas estan van fuera porque me sirven para ambos archivos

arch = open("boletas.txt","r",encoding="utf-8")
linea = arch.readline().strip()


while linea != "":
    # contadores solo para el archivo boletas
    contCafeL = 0
    contEmpL = 0
    contChapL = 0
    contAguaL = 0
    contGallL = 0
    contMuffL = 0
    contBebL = 0
    contSandL = 0
    
    fecha, hora, preciototal, cantProductos = partes(linea)
    totalProductos += cantProductos

    for i in range(cantProductos):
        linea = arch.readline().strip()
        item, precio = dividir(linea)
        if item == "cafe": # Aqui le sumo a ambos contadores y a los precios
            contCafe += 1
            contCafeL += 1
            montoCafe += contCafeL * precio
        if item == "empanada":
            contEmpL += 1
            contEmp += 1
            montoEmp += contEmpL * precio
        if item == "chaparrita":
            contChap += 1
            contChapL += 1
            montoChap += contChapL * precio
        if item == "sandwich":
            contSandL += 1
            contSand += 1
            montoSand += contSandL * precio
        if item == "agua":
            contAgua += 1
            contAguaL += 1
            montoAgua += contAguaL * precio
        if item == "galleta":
            contGall += 1
            contGallL += 1
            montoGall += contGallL * precio
        if item == "muffin":
            contMuff += 1
            contMuffL += 1
            montoMuff += contMuffL * precio
        if item == "bebida":
            contBeb += 1
            contBebL += 1
            montoBeb += contBebL * precio

    linea = arch.readline().strip()

arch.close() # Esto es para reusar la variable arch, pero podrias ponerle arch2
arch = open("libro_de_ventas.txt", "r", encoding = "utf-8")
linea = arch.readline().strip()

while linea != "":
    dividir = linea.split(",")
    item = dividir[0]
    precio = int(dividir[1])
    unidadesvendidas = int(dividir[2])
    totalProductos += unidadesvendidas
    if item == "cafe": # Lo mismo que en el otro archivo
        contCafe += unidadesvendidas
        contCafeL = unidadesvendidas
        montoCafe += contCafeL * precio
    if item == "empanada":
        contEmp += unidadesvendidas
        contEmpL = unidadesvendidas
        montoEmp += contEmpL * precio
    if item == "chaparrita":
        contChap += unidadesvendidas
        contChapL = unidadesvendidas
        montoChap += contChapL * precio
    if item == "agua":
        contAgua += unidadesvendidas
        contAguaL = unidadesvendidas 
        montoAgua += contAguaL * precio
    if item == "sandwich":
        contSand += unidadesvendidas
        contSandL = unidadesvendidas 
        montoSand += contSandL * precio
    if item == "galleta":
        contGall += unidadesvendidas
        contGallL = unidadesvendidas
        montoGall += contGallL * precio
    if item == "muffin":
        contMuff += unidadesvendidas
        contMuffL = unidadesvendidas
        montoMuff += contMuffL * precio
    if item == "bebida":
        contBeb += unidadesvendidas
        contBebL = unidadesvendidas
        montoBeb += contBebL * precio
    linea = arch.readline().strip()

print("1- Total de Ventas por Producto:") # Si lo imprimes no me da igual que a la prueba
# Pero me pusieron 0.97 puntos asi que tan perfecto no está

print(f"cafe: {contCafe} vendidos. Total: ${montoCafe}")
print(f"empanada: {contEmp} vendidos. Total: ${montoEmp}")
print(f"chaparrita: {contChap} vendidos. Total: ${montoChap}")
print(f"agua: {contAgua} vendidos. Total: ${montoAgua}")
print(f"galleta: {contGall} vendidos. Total: ${montoGall}")
print(f"sandwich: {contSand} vendidos. Total: ${montoSand}")
print(f"muffin: {contMuff} vendidos. Total: ${montoMuff}")
print(f"bebida: {contBeb} vendidos. Total: ${montoBeb}")


total = montoCafe + montoEmp + montoChap+ montoAgua+ montoSand+ montoGall+ montoMuff + montoBeb
promedio = int(total/totalProductos) # sin el int no funcionaba recuerdo

print(f"2- Total de Ventas: ${total}")
print(f"3- Monto promedio por ítem vendido: {promedio}")

IVA = total * 0.19
montoNeto = total - IVA
total = IVA + montoNeto
#no supe sacar el iva oremos

print("4- Detalle IVA monto de venta:")
print(f"- Total neto: {montoNeto}")
print(f"- IVA: {IVA}")
print(f"- Total con IVA: ${total} ")
