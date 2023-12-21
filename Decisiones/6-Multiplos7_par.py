num = input("Ingrese un número: ")

try:
    num_entero = int(num)

    if num_entero % 7 == 0 and num_entero % 2 == 0:
        print(f"{num_entero} es múltiplo de 7 y también es par.")
    elif num_entero % 7 == 0:
        print(f"{num_entero} es múltiplo de 7 pero no es par.")
    elif num_entero % 2 == 0:
        print(f"{num_entero} es par pero no es múltiplo de 7.")
    else:
        print(f"{num_entero} no es múltiplo de 7 ni es par.")
except ValueError:
    print("Por favor, ingrese un número entero válido.")