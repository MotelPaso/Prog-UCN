

pi = 3.1415
figura = input("Elige una figura, puede ser Triangulo, Cuadrado o Circulo: ")

if figura == "Triangulo":
    altura = float(input("Altura? "))
    base = float(input("Base? "))
    area = altura * base * (1/2)
    print(f"El area es {area}")
elif figura == "Cuadrado":
    print("hazlo")
elif figura == "Circulo":
    print("hazlo")
else:
    print("Figura no encontrada")