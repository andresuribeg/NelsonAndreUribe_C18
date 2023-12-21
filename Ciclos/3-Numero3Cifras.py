while True:
    try:
        numero = int(input("Ingrese un número: "))
        
        if 100 <= numero <= 999:
            print(f"Ha ingresado un número positivo de 3 cifras: {numero}")
            break  
        else:
            print("Por favor, ingrese un número positivo de 3 cifras.")
    except ValueError:
        print("Por favor, ingrese un número válido.")
