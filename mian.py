def dibujar_rectangulo():
    altura = int(input("Altura: "))
    ancho = int(input("Ancho: "))
    for _ in range(altura):
        print('*' * ancho)

def dibujar_triangulo():
    altura = int(input("Altura: "))
    for i in range(1, altura + 1):
        print('*' * i)

def dibujar_hexagono():
    lado = int(input("Lado: "))
    # Parte superior del hexágono
    for i in range(lado):
        print(' ' * (lado - i - 1) + '*' * (2 * i + 2))
    # Parte inferior del hexágono
    for i in range(lado - 1):
        print(' ' * (i + 1) + '*' * (2 * (lado - i - 1) + 2))

def main():
    print("¿Qué figura deseas dibujar?")
    print("1. Rectángulo")
    print("2. Triángulo")
    print("3. Hexágono")
    
    opcion = int(input("Selecciona una opción (1, 2 o 3): "))
    
    if opcion == 1:
        dibujar_rectangulo()
    elif opcion == 2:
        dibujar_triangulo()
    elif opcion == 3:
        dibujar_hexagono()
    else:
        print("Opción no válida. Por favor, elige 1, 2 o 3.")

# Ejecutar el programa
main()