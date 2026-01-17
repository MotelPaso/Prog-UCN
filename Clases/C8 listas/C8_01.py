
def Unicos(lista):
    listaUnicos = []
    for i in lista:
        if i not in listaUnicos:
            listaUnicos.append(i)
    return listaUnicos

lista = []
arch = open('nombres.txt', 'r', encoding = 'utf-8')
linea = arch.readline().strip()

while linea != '':
    lista.append(linea)
    linea = arch.readline().strip()

print(Unicos(lista))