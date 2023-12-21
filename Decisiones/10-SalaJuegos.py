class SalaDeJuegos:
    def __init__(self, coins):
        self.coins = coins

    def ingreso_salas(self):
        if self.coins == 4:
            print("¡Bienvenido! Puedes acceder a todas las salas: Consolas, Juegos 2D, Juegos 3D, Realidad Virtual.")
        elif self.coins == 3:
            print("¡Bienvenido! Puedes acceder a las tres primeras salas: Consolas, Juegos 2D, Juegos 3D.")
        elif self.coins == 2:
            print("¡Bienvenido! Puedes acceder a las dos primeras salas: Consolas, Juegos 2D.")
        elif self.coins == 1:
            print("¡Bienvenido! Puedes acceder a la primera sala: Consolas.")
        else:
            print("No tienes suficientes créditos para acceder a ninguna sala.")

if __name__ == "__main__":
    try:
        coins_usuario = int(input("Ingrese la cantidad de créditos que tiene el usuario: "))
        sala = SalaDeJuegos(coins_usuario)
        sala.ingreso_salas()
    except ValueError:
        print("Por favor, ingrese una cantidad válida de créditos.")