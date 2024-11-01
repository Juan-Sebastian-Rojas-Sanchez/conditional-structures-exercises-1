
def estimar_pi(n):
    pi_est = 0  # Inicializa la estimación de pi
    for k in range(n):
        # Calcula el término correspondiente de la serie
        term = ((-1) ** k) / (2 * k + 1)
        pi_est += term  # Suma el término a la estimación de pi
    pi_est *= 4  # Multiplica por 4 para obtener π
    return pi_est

def main():
    n = int(input("Ingrese el número de términos (n): "))
    pi_estimado = estimar_pi(n)
    print(pi_estimado)

# Ejecutar el programa
main()