
def Unicos(lista):
    listaUnicos = []
    for i in lista:
        if i not in listaUnicos:
            listaUnicos.append(i)
    return listaUnicos

def Repetidos(lista1,lista2):
    listaRepetidos = []
    num1 = len(lista1)
    num2 = len(lista2)
    if num1 > num2:
        for i in lista1:
            if i in lista2:
                listaRepetidos.append(i)
    elif num2 >= num1:
        for i in lista2:
            if i in lista1:
                listaRepetidos.append(i)
    return listaRepetidos

lista = []

arch = open('nombres.txt', 'r', encoding = 'utf-8')
linea = arch.readline().strip()

while linea != '':
    lista.append(linea)
    linea = arch.readline().strip()
unicos1 = Unicos(lista)


lista = []
arch = open('nombres2.txt', 'r', encoding = 'utf-8')
linea = arch.readline().strip()

while linea != '':
    lista.append(linea)
    linea = arch.readline().strip()
unicos2 = Unicos(lista)
# Creo que esto se podria hacer mejor con un def pero por ahora no me importa ^^

print(Repetidos(unicos1,unicos2))
