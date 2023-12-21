num = input("Ingrese un número: ")

try:
    num_entero = int(num)

    if num_entero < 0 and num_entero % 2 == 0:
        print(f"{num_entero} es un número negativo y par.")
    elif num_entero < 0:
        print(f"{num_entero} es un número negativo pero no es par.")
    elif num_entero % 2 == 0:
        print(f"{num_entero} es par pero no es negativo.")
    else:
        print(f"{num_entero} no es negativo ni es par.")
except ValueError:
    print("Por favor, ingrese un número entero válido.")
