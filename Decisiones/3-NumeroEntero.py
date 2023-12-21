num = input("Ingrese un número entero: ")

try:
    num_float = float(num)  
    num_entero = int(num_float)  

    if num_float == num_entero:
        print(f"{num} es un número entero.")
    else:
        print(f"{num} no es un número entero.")
except ValueError:
    print("Por favor, ingrese un número válido.")
