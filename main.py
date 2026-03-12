def calcular():
    peso = float(input("ingrese su peso en kilogramos:"))
    altura = float(input("ingrese su altura en metros: "))
    imc = peso / (altura ** 2)
    print("su indice de masa corporal es: ", imc)


while True:
    print("bienvenido al calculador de indice de masa corporal")
    print(f"hola {input('ingrese su nombre: ')} bienvenido al calculador de indice de masa corporal")
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
        
