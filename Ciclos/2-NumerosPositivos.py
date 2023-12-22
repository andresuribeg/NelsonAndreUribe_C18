while True:
    try:
        num = float(input("Ingrese un número: "))
        if num > 0:
            print(f"Has ingresado elnúmero positivo: {num}")
            break  # Sale del bucle si se ingresa un número positivo
        else:
            print("Por favor, ingrese un número positivo (mayor que cero)")
    except ValueError:
        print("Por favor, ingrese un número válido.")