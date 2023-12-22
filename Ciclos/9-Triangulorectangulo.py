try:
    altura = int(input("Ingrese la altura del triángulo (número entero): "))
    
    for i in range(1, altura * 2, 2):
        for j in range(i, 0, -2):
            print(j, end=" ")
        print()
except ValueError:
    print("Por favor, ingrese un número entero válido.")
