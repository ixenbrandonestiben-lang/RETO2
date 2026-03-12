def calcular():
    peso = float(input("ingrese su peso en kilogramos:"))
    altura = float(input("ingrese su altura en metros: "))
    imc = peso / (altura ** 2)
    print("su indice de masa corporal es: ", imc)

