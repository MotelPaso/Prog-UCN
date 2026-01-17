
def Malware(texto,lista):
    if 'ware' in texto:
        lista[0] += 1
    if 'Phis' in texto:
        lista[1] += 1
    if 'SQL' in texto:
        lista[2] += 1
    if 'DDoS' in texto:
        lista[3] += 1
    return lista

def Efectividad(cont,ataque,costo):
    if ataque >= 60:
        cont += 1
    if ataque <= 60:
        costo += 0.1
    elif ataque > 60 and ataque < 95:
        costo += 0.3
    elif ataque >= 95:
        costo += 1
    return cont, costo

def MaximoLista(lista): # lista se ve como [0,1,0,1]
    maximo = 0
    indice_maximo2 = 0
    for k in range(len(lista)):
        if lista[k] > maximo: # Sacamos el primer maximo
            maximo = lista[k]
            indice_maximo = k
        if lista[k] >= maximo: # Luego, sacamos el igual al maximo, si es que existe
            indice_maximo2 = k
    return maximo, indice_maximo2, indice_maximo

def mostrarAtaques(indice):
    if indice == 0:
        print('- El ataque mas recurrente en',pais,'es Malware')
    if indice == 1:
        print('- El ataque mas recurrente en',pais,'es Phishing')
    if indice == 2:
        print('- El ataque mas recurrente en',pais,'es SQLInjection')
    if indice == 3:
        print('- El ataque mas recurrente en',pais,'es DDoS')

arch = open('ataques.txt', 'r', encoding= 'utf-8')
linea = arch.readline().strip()

promedios = []
maximoContinente = 0
while linea != "":
    partes = linea.split(';')
    continente = partes[0]
    cantPaises = int(partes[1])
    contEffectGlobal = 0
    costoTotal = 0
    ataquesTotal = 0
    promedioConti = 0
    # Revision por pais
    for i in range(cantPaises):
        linea = arch.readline().strip()
        division = linea.split(',')
        pais = division[0]
        lista = [0,0,0,0]
        cantAtaques = int(division[1])
        ataquesTotal += cantAtaques
        contEffectLocal = 0
        # Revision de ataques
        for j in range(0,cantAtaques*2,2):
            lista = Malware(division[j+2], lista)

            efectivo = int(division[j+3])
            contEffectGlobal, costoTotal = Efectividad(contEffectGlobal,efectivo,costoTotal)
            contEffectLocal += efectivo

        maximo, maximo2, indice = MaximoLista(lista)
        if maximo2 == indice: # Si son iguales maximo1,maximo2
            mostrarAtaques(indice)
        elif maximo2 != indice:
            print('- El ataque mas recurrente en',pais,'es Variado')
        promedio = contEffectLocal / cantAtaques
        promedioConti += promedio
        print('  El promedio de efectividad fue de', promedio)

        if promedio <= 60:
            costoTotal += 0.1
        elif promedio > 60 and promedio < 95:
            costoTotal += 0.3
        elif promedio >= 95:
            costoTotal += 1

    promedioConti /= cantPaises
    if promedioConti > maximoContinente:
        maximoContinente = promedioConti
        continenteMaximo = continente

    if contEffectGlobal == ataquesTotal:
        print(f'* Desastre TOTAL, es urgente mejorar los recursos defensivos de {continente} *')
    print('La cantidad de ataques efectivos en', continente, 'fue de:', contEffectGlobal)
    print(f'El costo total en reparaciones fue de ${round(costoTotal,1)} M')
    print()

    linea = arch.readline().strip()

print(f'El proximo continente foco de los ataques de Anonymous posiblemente sea {continenteMaximo} con promedio de efectividad de {round(maximoContinente,2)}%')

