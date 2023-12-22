try:
    edad = int(input("Ingrese su edad: "))

    if edad <= 0:
        print("Por favor, ingrese una edad válida.")
    else:
        print("Años que ha cumplido:")
        for i in range(1, edad + 1):
            print(i)
except ValueError:
    print("Por favor, ingrese un número entero válido para la edad.")
