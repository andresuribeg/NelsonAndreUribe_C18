class Restaurante:
    def __init__(self):
        self.menu = {
            "carne": "Vino tinto",
            "pescado": "Vino blanco",
            "verdura": "Agua"
        }

    def tomar_pedido(self, eleccion):
        eleccion_lower = eleccion.lower()

        if eleccion_lower in self.menu:
            bebida = self.menu[eleccion_lower]
            print(f"Has elegido {eleccion_lower} te sugiero {bebida}.")
        else:
            print("Elija carne, pescado o verdura.")

if __name__ == "__main__":
    restaurante = Restaurante()

    eleccion_cliente = input("¿Seleccione el menú de su preferencia (carne, pescado o verdura)? ")

    restaurante.tomar_pedido(eleccion_cliente)
