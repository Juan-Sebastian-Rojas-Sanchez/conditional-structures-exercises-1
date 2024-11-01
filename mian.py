#Tiempo de viaje
def calcular_tiempo_viaje():
    while True:
        total_minutos = 0
        
        while True:
            # Solicitar la duración del tramo
            duracion_tramo = int(input("Duracion tramo: "))
            if duracion_tramo == 0:
                break  # Salir del bucle si se ingresa 0
            total_minutos += duracion_tramo
        
        # Calcular horas y minutos
        horas = total_minutos // 60
        minutos = total_minutos % 60
        
        # Mostrar el resultado
        print(f"Tiempo total de viaje: {horas}:{minutos:02d} horas")

# Llamar a la función
calcular_tiempo_viaje()