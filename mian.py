def collatz_sequence(n):
    """Genera la secuencia de Collatz para un número entero n."""
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n //= 2  # Si es par
        else:
            n = 3 * n + 1  # Si es impar
    sequence.append(1)  # Agregar el último número de la secuencia
    return sequence

def collatz_length(n):
    """Devuelve la longitud de la secuencia de Collatz para el número n."""
    return len(collatz_sequence(n))

def main():
    user_input = int(input("Ingrese un número entero positivo: "))
    
    # Mostrar la secuencia de Collatz para el número ingresado
    print("Secuencia de Collatz:")
    sequence = collatz_sequence(user_input)
    print(" ".join(map(str, sequence)))

    # Graficar los largos de las secuencias de Collatz
    print("\nLongitudes de las secuencias de Collatz:")
    for i in range(1, user_input + 1):
        length = collatz_length(i)
        print(f"{i} {'*' * length}")

# Ejecutar el programa
main()