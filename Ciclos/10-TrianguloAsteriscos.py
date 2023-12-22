try:
    altura = int(input("Ingrese la altura del triángulo (número entero): "))
    
    for i in range(1, altura + 1):
        print("*" * i)
except ValueError:
    print("Por favor, ingrese un número entero válido.")