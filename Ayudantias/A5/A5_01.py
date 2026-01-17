
def ContarPalabras(palabra):
    palabra = palabra.split(' ')
    return len(palabra)

palabra = input('Ingrese su oracion aqui: ')

print(ContarPalabras(palabra))