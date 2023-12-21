num = input("Ingrese un numero entero: ")

try:
    num_entero = int(num)

    if num_entero % 2 != 0 and num_entero % 5 == 0:
        print("El número es impar y múltiplo de 5.")
    elif num_entero % 2 == 0 and num_entero % 5 == 0:
        print("El número es par y es múltiplo de 5.")
    elif num_entero % 2 == 0 and num_entero % 5 != 0:
        print("El número es par pero no es múltiplo de 5.")
    elif num_entero % 2 != 0 and num_entero % 5 != 0:
        print("El número no es par ni es múltiplo de 5.")
    
except ValueError:
    print("Por favor, ingrese un número entero válido.")
