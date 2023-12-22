def tabla_de_multiplicar(multiplicando):
    print(f"Tabla de multiplicar del {multiplicando}:")
    for i in range(1, 11):
        producto = multiplicando * i
        print(f"{multiplicando} x {i} = {producto}")


try:
    num = int(input("Ingrese un número para generar la tabla de multiplicar: "))
    tabla_de_multiplicar(num)
except ValueError:
    print("Por favor, ingrese un número entero válido.")
