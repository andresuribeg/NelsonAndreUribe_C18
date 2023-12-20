num = input("Ingrese un numero entero: ")

try:
    num_entero = int(num)

    if num_entero % 6 == 0:
        print("El número es par y múltiplo de 6")
    elif num_entero % 2 == 0:
        print("El número es par pero no es múltiplo de 6")
    else:
        print("El número no es par ni es múltiplo de 6")

except ValueError:
    print("Por favor, ingrese un número entero válido.")