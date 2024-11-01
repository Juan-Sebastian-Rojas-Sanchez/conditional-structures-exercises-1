
def factorial(n):
    """Calcula el factorial de n de manera recursiva."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def estimar_e():
    """Calcula una aproximación del número de Euler (e) usando la suma de factoriales."""
    suma = 0.0
    n = 10  # Comenzamos desde 10!
    
    while True:
        termino_actual = factorial(n)
        suma += termino_actual
        n += 1
        # Calcular el siguiente término para comprobar la diferencia
        termino_siguiente = factorial(n)
        
        # Verificar la diferencia entre los términos
        if abs(termino_siguiente - termino_actual) < 0.0001:
            break
            
    return suma

def main():
    e_estimado = estimar_e()
 print(f"Valor aproximado de e: {e_estimado}")
