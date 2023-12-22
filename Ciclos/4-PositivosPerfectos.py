def es_numero_perfecto(num):
    suma_divisores = 0

    for i in range(1, num):
        if num % i == 0:
            suma_divisores += i

    return suma_divisores == num

try:
    num_usuario = int(input("Ingrese un número positivo: "))

    if num_usuario > 0:
        if es_numero_perfecto(num_usuario):
            print(f"{num_usuario} es un número perfecto.")
        else:
            print(f"{num_usuario} no es un número perfecto.")
    else:
        print("Por favor, ingrese un número positivo.")
except ValueError:
    print("Por favor, ingrese un número válido.")
