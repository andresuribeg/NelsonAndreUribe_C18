def determinar_ganador(jugador1, jugador2):
    if jugador1 == jugador2:
        return "Empate"
    elif (jugador1 == "piedra" and jugador2 == "tijera") or \
         (jugador1 == "papel" and jugador2 == "piedra") or \
         (jugador1 == "tijera" and jugador2 == "papel"):
        return "Jugador 1 gana"
    else:
        return "Jugador 2 gana"

def juego_piedra_papel_tijera():
    print("Bienvenido al juego de piedra, papel o tijera.")
    jugador1 = input("Jugador 1, seleccione piedra, papel o tijera: ").lower()
    jugador2 = input("Jugador 2, seleccione piedra, papel o tijera: ").lower()

    if jugador1 not in ["piedra", "papel", "tijera"] or jugador2 not in ["piedra", "papel", "tijera"]:
        print("Ingresa opciones válidas: piedra, papel o tijera.")
    else:
        resultado = determinar_ganador(jugador1, jugador2)
        print(resultado)

juego_piedra_papel_tijera()
