class Combos:
    def __init__(self):
        self.menu_combos = {
            1: "Combo de hamburguesas de carne al horno con limonada de coco",
            2: "Combo de perro caliente con papas a la francesa y gaseosa",
            3: "Combo ensalada tropical con limonada de hierbabuena",
        }

    def mostrar_menu(self):
        print("Menú de Combos:")
        for num, combo in self.menu_combos.items():
            print(f"{num}. {combo}")

    def ordenar_combo(self, numero_combo):
        if numero_combo in self.menu_combos:
            combo_seleccionado = self.menu_combos[numero_combo]
            print("")
            print(f"Has ordenado: {combo_seleccionado}. ¡Tu pedido se entregará en 15 minutos!")
            print("")
            
        else:
            print("Opción no válida. Por favor, elige un número válido del menú.")
                        


restaurante = Combos()

restaurante.mostrar_menu()
seleccion = input("Ingrese el número del combo que desea (0 para salir): ")

try:
    numero_combo = int(seleccion)
    if numero_combo == 0:
        print("Gracias por visitarnos!")
    else:
            restaurante.ordenar_combo(numero_combo)
except ValueError:
    print("Por favor, ingrese un número válido.")
