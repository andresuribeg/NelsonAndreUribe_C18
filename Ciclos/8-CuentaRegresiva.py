from datetime import datetime, timedelta
import time

def contar_regresivo(horas, minutos, segundos):
    tiempo_objetivo = datetime.now() + timedelta(hours=horas, minutes=minutos, seconds=segundos)
    
    while datetime.now() < tiempo_objetivo:
        tiempo_restante = tiempo_objetivo - datetime.now()
        print(f"Tiempo restante: {tiempo_restante}")
        time.sleep(1)  # Espera 1 segundo antes de la próxima iteración
    
    print("¡Conteo regresivo completado!")

if __name__ == "__main__":
    horas = 0 
    minutos = 0
    segundos = 10
    
    contar_regresivo(horas, minutos, segundos)
