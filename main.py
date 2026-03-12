def calcular():
    peso = float(input("ingrese su peso en kilogramos:"))
    altura = float(input("ingrese su altura en metros: "))
    imc = peso / (altura ** 2)
    print("su indice de masa corporal es: ", imc)

def separador():
    print("--------------------------------------------------") 
while True:
    separador()
    print("bienvenido al calculador de indice de masa corporal")
    separador()
    nombre = input("ingrese su nombre: ")
    separador()
    print("Hola ", nombre, "bienvenido a nuestra calculador de IMC")
    separador()
    print("1. calcular indice de masa corporal")
    print("2. salir")
    opcion = input("ingrese su opcion: ")
    if opcion == "1":
        calcular()
    elif opcion == "2":
        print("gracias por usar el calculador de indice de masa corporal")
        break
    else:
        print("opcion no valida, por favor intente de nuevo")
        
