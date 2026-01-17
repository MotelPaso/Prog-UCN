
# esto es el desafio 5, es un ejemplo de lo que no se debe hacer
# por esto es importante dividirlo en funciones separadas.

import numpy as np
from math import sin, cos

n_paises=[]
paises=[]
cont_tiempo=1
lista_Rtarifa=[0,0]
cont_tarifas_coste_total=0
cont_costes_totales=0
cont_pais1=0
cont_pais2=0
cont_pais3=0
cont_pais4=0
mayor_material_transportado=-1
mayor_lluvia=0
mayor_lluvia_posicion=[0,0]
mayor_lluvia_tiempo=0
lista_mayor_material=[]
lista_mayor_material_paises=[]
lista_mayor_material_fil=[]
lista_mayor_material_col=[]
lista_pais_mayor=[]
lista_material_paises=[]
pais_1_material=0
pais_2_material=0
pais_3_material=0
pais_4_material=0
pais_1=0
pais_2=0
pais_3=0
pais_4=0
continente=0
continente_materiales=0
arch=open("Desafio05.txt","r",encoding="utf-8")
linea=arch.readline().strip()
partes=linea.split(",")
fila=int(partes[0])
columna=int(partes[1])
posc_camion=[fila-1,0]
linea=arch.readline().strip()
if linea=="Países":
    linea=arch.readline().strip()
    while linea!="Fin Países":
        partes1=linea.split(":")
        n_paises.append(partes1[0])
        paises.append(partes1[1])
        linea=arch.readline().strip()
linea=arch.readline().strip()
if linea=="Mapa":
    linea=arch.readline().strip()
    matriz_mapa=np.zeros((fila,columna))
    cont_f=0
    while linea!="Fin Mapa":
        partes2=linea.split(",")
        for i in range(columna):
            matriz_mapa[cont_f][i]=partes2[i]
        cont_f+=1        
        linea=arch.readline().strip()
linea=arch.readline().strip()
if linea=="Tarifas":
    linea=arch.readline().strip()
    matriz_tarifa=[]
    while linea!="Fin Tarifas":
        lista_tarifa=[]
        partes3=linea.split(",")
        pais1=partes3[0]
        pais2=partes3[1]
        tarifa=int(partes3[2])
        if pais1==paises[0]:
            lista_tarifa.append(1)
            lista_tarifa.append(pais1)
        if pais1==paises[1]:
            lista_tarifa.append(2)
            lista_tarifa.append(pais1)
        if pais1==paises[2]:
            lista_tarifa.append(3)
            lista_tarifa.append(pais1)
        if pais1==paises[3]:
            lista_tarifa.append(4)
            lista_tarifa.append(pais1)
        if pais2==paises[0]:
            lista_tarifa.append(1)
            lista_tarifa.append(pais2)
        if pais2==paises[1]:
            lista_tarifa.append(2)
            lista_tarifa.append(pais2)
        if pais2==paises[2]:
            lista_tarifa.append(3)    
            lista_tarifa.append(pais2)
        if pais2==paises[3]:
            lista_tarifa.append(4)
            lista_tarifa.append(pais2)
        lista_tarifa.append(tarifa)
        matriz_tarifa.append(lista_tarifa)
        linea=arch.readline().strip()
linea=arch.readline().strip()
if linea=="Terreno":
    linea=arch.readline().strip()
    matriz_terreno=np.zeros((fila,columna))
    cont_terrenos=0
    while linea!="Fin Terreno":
        partes4=linea.split(",")
        for k in range(columna):
            matriz_terreno[cont_terrenos][k]=int(partes4[k])                 
        cont_terrenos+=1
        linea=arch.readline().strip()
linea=arch.readline().strip()
if linea=="Material":
    linea=arch.readline().strip()
    cont_materiales=0
    matriz_materiales=np.zeros((fila,columna))
    while linea!="Fin Material":
        partes5=linea.split(",")
        for j in range(columna):
            matriz_materiales[cont_materiales][j]=int(partes5[j])
        cont_materiales+=1
        linea=arch.readline().strip()
linea=arch.readline().strip()
while linea!="":
    partes_papu=linea.split(",") # poco serio
    viaje_n=partes_papu[0]
    cargas=int(partes_papu[1])
    cantidad_mov=int(partes_papu[2])
    cont_litros_bencina=0
    cont_tarifas_coste=0
    matriz_materiales[posc_camion[0]][posc_camion[1]]-=cargas
    print(f"{viaje_n} - carga:{float(cargas)} ton")
    linea=arch.readline().strip()
    for t in range(cantidad_mov):
        if linea=="Derecha":
            posc_camion[1]+=1
            tarifa_total=0
            lista_Rtarifa[1]=matriz_mapa[posc_camion[0]][posc_camion[1]]
            lista_Rtarifa[0]=matriz_mapa[posc_camion[0]][posc_camion[1]-1]
            for a in range(len(matriz_tarifa)):
                if lista_Rtarifa[0]==matriz_tarifa[a][0] and lista_Rtarifa[1]==matriz_tarifa[a][2]:
                    tarifa_total=matriz_tarifa[a][4]
                    cont_tarifas_coste+=tarifa_total
                    cont_tarifas_coste_total+=tarifa_total
                    if lista_Rtarifa[1]==1:
                        cont_pais1+=1
                    if lista_Rtarifa[1]==2:
                        cont_pais2+=1
                    if lista_Rtarifa[1]==3:
                        cont_pais3+=1
                    if lista_Rtarifa[1]==4:
                        cont_pais4+=1
                    print(f"--Aduana de {matriz_tarifa[a][1]} a {matriz_tarifa[a][3]}: ${float(tarifa_total)}--")
                elif lista_Rtarifa[0]==matriz_tarifa[a][2] and lista_Rtarifa[1]==matriz_tarifa[a][0]:
                    tarifa_total=matriz_tarifa[a][4]
                    cont_tarifas_coste+=tarifa_total
                    cont_tarifas_coste_total+=tarifa_total
                    if lista_Rtarifa[1]==1:
                        cont_pais1+=1
                    if lista_Rtarifa[1]==2:
                        cont_pais2+=1
                    if lista_Rtarifa[1]==3:
                        cont_pais3+=1
                    if lista_Rtarifa[1]==4:
                        cont_pais4+=1
                    print(f"--Aduana de {matriz_tarifa[a][3]} a {matriz_tarifa[a][1]}: ${float(tarifa_total)}--")
        if linea=="Izquierda":
            posc_camion[1]-=1
            tarifa_total=0
            lista_Rtarifa[1]=matriz_mapa[posc_camion[0]][posc_camion[1]]
            lista_Rtarifa[0]=matriz_mapa[posc_camion[0]][posc_camion[1]+1]
            for a in range(len(matriz_tarifa)):
                if lista_Rtarifa[0]==matriz_tarifa[a][0] and lista_Rtarifa[1]==matriz_tarifa[a][2]:
                    tarifa_total=matriz_tarifa[a][4]
                    cont_tarifas_coste+=tarifa_total
                    cont_tarifas_coste_total+=tarifa_total
                    if lista_Rtarifa[1]==1:
                        cont_pais1+=1
                    if lista_Rtarifa[1]==2:
                        cont_pais2+=1
                    if lista_Rtarifa[1]==3:
                        cont_pais3+=1
                    if lista_Rtarifa[1]==4:
                        cont_pais4+=1
                    print(f"--Aduana de {matriz_tarifa[a][1]} a {matriz_tarifa[a][3]}: ${float(tarifa_total)}--")
                elif lista_Rtarifa[0]==matriz_tarifa[a][2] and lista_Rtarifa[1]==matriz_tarifa[a][0]:
                    tarifa_total=matriz_tarifa[a][4]
                    cont_tarifas_coste+=tarifa_total
                    cont_tarifas_coste_total+=tarifa_total
                    if lista_Rtarifa[1]==1:
                        cont_pais1+=1
                    if lista_Rtarifa[1]==2:
                        cont_pais2+=1
                    if lista_Rtarifa[1]==3:
                        cont_pais3+=1
                    if lista_Rtarifa[1]==4:
                        cont_pais4+=1
                    print(f"--Aduana de {matriz_tarifa[a][3]} a {matriz_tarifa[a][1]}: ${float(tarifa_total)}--")
        if linea=="Arriba":
            posc_camion[0]-=1
            tarifa_total=0
            lista_Rtarifa[1]=matriz_mapa[posc_camion[0]][posc_camion[1]]
            lista_Rtarifa[0]=matriz_mapa[posc_camion[0]+1][posc_camion[1]]
            for a in range(len(matriz_tarifa)):
                if lista_Rtarifa[0]==matriz_tarifa[a][0] and lista_Rtarifa[1]==matriz_tarifa[a][2]:
                    tarifa_total=matriz_tarifa[a][4]
                    cont_tarifas_coste+=tarifa_total
                    cont_tarifas_coste_total+=tarifa_total
                    if lista_Rtarifa[1]==1:
                        cont_pais1+=1
                    if lista_Rtarifa[1]==2:
                        cont_pais2+=1
                    if lista_Rtarifa[1]==3:
                        cont_pais3+=1
                    if lista_Rtarifa[1]==4:
                        cont_pais4+=1
                    print(f"--Aduana de {matriz_tarifa[a][1]} a {matriz_tarifa[a][3]}: ${float(tarifa_total)}--")
                elif lista_Rtarifa[0]==matriz_tarifa[a][2] and lista_Rtarifa[1]==matriz_tarifa[a][0]:
                    tarifa_total=matriz_tarifa[a][4]
                    cont_tarifas_coste+=tarifa_total
                    cont_tarifas_coste_total+=tarifa_total
                    if lista_Rtarifa[1]==1:
                        cont_pais1+=1
                    if lista_Rtarifa[1]==2:
                        cont_pais2+=1
                    if lista_Rtarifa[1]==3:
                        cont_pais3+=1
                    if lista_Rtarifa[1]==4:
                        cont_pais4+=1
                    print(f"--Aduana de {matriz_tarifa[a][3]} a {matriz_tarifa[a][1]}: ${float(tarifa_total)}--")

        if linea=="Abajo":
            posc_camion[0]+=1
            tarifa_total=0
            lista_Rtarifa[1]=matriz_mapa[posc_camion[0]][posc_camion[1]]
            lista_Rtarifa[0]=matriz_mapa[posc_camion[0]-1][posc_camion[1]-1]
            for a in range(len(matriz_tarifa)):
                if lista_Rtarifa[0]==matriz_tarifa[a][0] and lista_Rtarifa[1]==matriz_tarifa[a][2]:
                    tarifa_total=matriz_tarifa[a][4]
                    cont_tarifas_coste+=tarifa_total
                    cont_tarifas_coste_total+=tarifa_total
                    if lista_Rtarifa[1]==1:
                        cont_pais1+=1
                    if lista_Rtarifa[1]==2:
                        cont_pais2+=1
                    if lista_Rtarifa[1]==3:
                        cont_pais3+=1
                    if lista_Rtarifa[1]==4:
                        cont_pais4+=1
                    print(f"--Aduana de {matriz_tarifa[a][1]} a {matriz_tarifa[a][3]}: ${float(tarifa_total)}--")
                elif lista_Rtarifa[0]==matriz_tarifa[a][2] and lista_Rtarifa[1]==matriz_tarifa[a][0]:
                    tarifa_total=matriz_tarifa[a][4]
                    cont_tarifas_coste+=tarifa_total
                    cont_tarifas_coste_total+=tarifa_total
                    if lista_Rtarifa[1]==1:
                        cont_pais1+=1
                    if lista_Rtarifa[1]==2:
                        cont_pais2+=1
                    if lista_Rtarifa[1]==3:
                        cont_pais3+=1
                    if lista_Rtarifa[1]==4:
                        cont_pais4+=1
                    print(f"--Aduana de {matriz_tarifa[a][3]} a {matriz_tarifa[a][1]}: ${float(tarifa_total)}--")
        lluvia=max(0, sin(posc_camion[0])*cos(posc_camion[1]) + cont_tiempo)
        if lluvia>mayor_lluvia:
            mayor_lluvia=lluvia
            mayor_lluvia_tiempo=cont_tiempo
            mayor_lluvia_posicion[0],mayor_lluvia_posicion[1]=posc_camion[0],posc_camion[1]
        cont_litros_bencina+=cargas * (matriz_terreno[posc_camion[0]][posc_camion[1]]+ 0.1) + 5 *lluvia
        print(f"(t: {cont_tiempo}) - {linea} - ({posc_camion[0]}, {posc_camion[1]}), Terreno: {matriz_terreno[posc_camion[0]][posc_camion[1]]}, Lluvia: {lluvia}, País: {matriz_mapa[posc_camion[0]][posc_camion[1]]}, Consumo: {cargas * (matriz_terreno[posc_camion[0]][posc_camion[1]]+ 0.1) + 5 *lluvia}")
        cont_tiempo+=1
        linea=arch.readline().strip()
    matriz_materiales[posc_camion[0]][posc_camion[1]]+= cargas
    cont_costes_totales+=(cont_litros_bencina*10)+cont_tarifas_coste 
    if matriz_mapa[fila-1][0]!=matriz_mapa[posc_camion[0]][posc_camion[1]]:
        if cargas>mayor_material_transportado:
            mayor_material_transportado=cargas
            if matriz_mapa[posc_camion[0]][posc_camion[1]]==1:
                nombre_mayor_material_transportado=paises[0]
            if matriz_mapa[posc_camion[0]][posc_camion[1]]==2:
                nombre_mayor_material_transportado=paises[1]
            if matriz_mapa[posc_camion[0]][posc_camion[1]]==3:
                nombre_mayor_material_transportado=paises[2] 
            if matriz_mapa[posc_camion[0]][posc_camion[1]]==4:
                nombre_mayor_material_transportado=paises[3]
    print(f"Fin {viaje_n} - Carga acumulada en ubicación final ({posc_camion[0]}, {posc_camion[1]}): {float(matriz_materiales[posc_camion[0]][posc_camion[1]])} ton ")
    print(f"Consumo total en el viaje: {cont_litros_bencina} litros")
    print(f"Dinero gastado: ${cont_litros_bencina*10} + ${cont_tarifas_coste} = ${(cont_litros_bencina*10) + cont_tarifas_coste}  ")
    print("----------------------")
for i in range(fila):
    for j in range(columna):
        if matriz_mapa[i][j]==1:
            pais_1+=1 
            continente+=1
            pais_1_material+=float(matriz_materiales[i][j])
            continente_materiales+=float(matriz_materiales[i][j])
        if matriz_mapa[i][j]==2:
            pais_2+=1 
            continente+=1
            pais_2_material+=float(matriz_materiales[i][j])
            continente_materiales+=float(matriz_materiales[i][j])
        if matriz_mapa[i][j]==3:
            pais_3+=1 
            continente+=1
            pais_3_material+=float(matriz_materiales[i][j])
            continente_materiales+=float(matriz_materiales[i][j])
        if matriz_mapa[i][j]==4:
            pais_4+=1 
            continente+=1
            pais_4_material+=float(matriz_materiales[i][j])
            continente_materiales+=float(matriz_materiales[i][j])
lista_pais_mayor.append(pais_1)
lista_pais_mayor.append(pais_2)
lista_pais_mayor.append(pais_3) 
lista_pais_mayor.append(pais_4)
lista_material_paises.append(pais_1_material)
lista_material_paises.append(pais_2_material)
lista_material_paises.append(pais_3_material)
lista_material_paises.append(pais_4_material)

for w in range(len(lista_pais_mayor)-1):
    for ww in range(w+1,len(lista_pais_mayor)):
        if lista_pais_mayor[w]<lista_pais_mayor[ww]:
            lista_pais_mayor[w],lista_pais_mayor[ww]=lista_pais_mayor[ww],lista_pais_mayor[w]
for m in range(len(lista_material_paises)-1):
    for mm in range(m+1,len(lista_material_paises)):
        if lista_material_paises[m]<lista_material_paises[mm]:
            lista_material_paises[m],lista_material_paises[mm]=lista_material_paises[mm],lista_material_paises[m]
print(f"2. Total gastado en aduanas: ${float(cont_tarifas_coste_total)}")
print("----------------------")
if cont_pais1>cont_pais2 and cont_pais1 >cont_pais3 and cont_pais1 >cont_pais4:
    print(f"3. País más visitado: {paises[0]} ({cont_pais1} visitas)")
if cont_pais2>cont_pais1 and cont_pais2 >cont_pais3 and cont_pais2 >cont_pais4:
    print(f"3. País más visitado: {paises[1]} ({cont_pais2} visitas)")
if cont_pais3>cont_pais2 and cont_pais3 >cont_pais1 and cont_pais3 >cont_pais4:
    print(f"3. País más visitado: {paises[2]} ({cont_pais3} visitas)")
if cont_pais4>cont_pais2 and cont_pais4 >cont_pais3 and cont_pais4 >cont_pais1:
    print(f"3. País más visitado: {paises[3]} ({cont_pais4} visitas)")
print("----------------------")
print(f"4. País con más carga recibida: {nombre_mayor_material_transportado} ({float(mayor_material_transportado)} toneladas)")
print("----------------------")
print(f"5. Momento más lluvioso: ({mayor_lluvia_posicion[0]}, {mayor_lluvia_posicion[1]}) (t: {mayor_lluvia_tiempo}) - Lluvia: {mayor_lluvia} mm ")
print("----------------------")
print(f"6. Dinero gastado en total: ${cont_costes_totales}")
print("----------------------")
print("7. Top 5 ubicaciones con mayor carga acumulada:")
for ii in range(fila):
    for jj in range(columna):
        lista_mayor_material.append(matriz_materiales[ii][jj])
        lista_mayor_material_fil.append(ii)
        lista_mayor_material_col.append(jj)
        if matriz_mapa[ii][jj]==1:
            lista_mayor_material_paises.append(paises[0])
        if matriz_mapa[ii][jj]==2:
            lista_mayor_material_paises.append(paises[1])
        if matriz_mapa[ii][jj]==3:
            lista_mayor_material_paises.append(paises[2])
        if matriz_mapa[ii][jj]==4:
            lista_mayor_material_paises.append(paises[3])
for lis in range(len(lista_mayor_material)-1):
    for ta in range(lis+1,len(lista_mayor_material)):  
        if lista_mayor_material[lis]<lista_mayor_material[ta]:
            lista_mayor_material[ta],lista_mayor_material[lis]=lista_mayor_material[lis],lista_mayor_material[ta]
            lista_mayor_material_paises[ta],lista_mayor_material_paises[lis]=lista_mayor_material_paises[lis],lista_mayor_material_paises[ta]
            lista_mayor_material_fil[ta],lista_mayor_material_fil[lis]=lista_mayor_material_fil[lis],lista_mayor_material_fil[ta]
            lista_mayor_material_col[ta],lista_mayor_material_col[lis]=lista_mayor_material_col[lis],lista_mayor_material_col[ta]
for zz in range(5):
    print(f"({lista_mayor_material_fil[zz]}, {lista_mayor_material_col[zz]}): {float(lista_mayor_material[zz])} toneladas - País: {lista_mayor_material_paises[zz]}")
print("----------------------")
print("8. Distribución del mapa político:") 
for www in range(len(lista_pais_mayor)):
    if lista_pais_mayor[www]==pais_1:
        print(f"{paises[0]}: {((lista_pais_mayor[www])/continente)*100}%")
    if lista_pais_mayor[www]==pais_2:
        print(f"{paises[1]}: {((lista_pais_mayor[www])/continente)*100}%")
    if lista_pais_mayor[www]==pais_3:
        print(f"{paises[2]}: {((lista_pais_mayor[www])/continente)*100}%")
    if lista_pais_mayor[www]==pais_4:
        print(f"{paises[3]}: {((lista_pais_mayor[www])/continente)*100}%")
print("----------------------")
print("9. Distribución de carga en países:")
for mmm in range(len(lista_material_paises)):
    if lista_material_paises[mmm]==pais_1_material:
        print(f"{paises[0]}: {lista_material_paises[mmm]} toneladas ({((lista_material_paises[mmm])/continente_materiales)*100}%)")
    if lista_material_paises[mmm]==pais_2_material:
        print(f"{paises[1]}: {lista_material_paises[mmm]} toneladas ({((lista_material_paises[mmm])/continente_materiales)*100}%)")    
    if lista_material_paises[mmm]==pais_3_material:
        print(f"{paises[2]}: {lista_material_paises[mmm]} toneladas ({((lista_material_paises[mmm])/continente_materiales)*100}%)")    
    if lista_material_paises[mmm]==pais_4_material:
        print(f"{paises[3]}: {lista_material_paises[mmm]} toneladas ({((lista_material_paises[mmm])/continente_materiales)*100}%)")    
print("----------------------")
