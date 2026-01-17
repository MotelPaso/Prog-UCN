

'''

print('SISTEMA DE REPORTES "TERMINAL DE BUSES GENERICO 33')

print('\nOrdenar reportes por')
print('1) Conductores [A-Z]')
print('2) Auxiliares [A-Z]')
print('3) Hora de salida [00-24]')
print('4) Destinos recurrentes [mayor-menor]')
print('5) Buscar por patente')
print('0) Cerrar Programa')
opcion = input('Seleccione opción: ')
print('')

'''

def ObtenerDatos(archivo):
    listaDatos = []
    arch = open(archivo, 'r', encoding='utf-8')
    linea = arch.readline().strip()
    while linea != "":
        listaDatos.append(linea)
        linea = arch.readline().strip()
    return listaDatos

def SepararDatos(datos,indice):
    listaPorOrdenar = []
    for i in range(len(datos)):
        listaInterna = datos[i].split(',')
        listaPorOrdenar.append(listaInterna[indice])
    return listaPorOrdenar

def OrdenarMenorMayor(lista):
    for i in range(len(lista) - 1):
        for j in range(i+1,len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


opcion = ''

listaDatos = ObtenerDatos('cronograma.txt')


print('Conductores por orden alfabético')
ConductoresOrdenados = SepararDatos(listaDatos,1)

print(ConductoresOrdenados)