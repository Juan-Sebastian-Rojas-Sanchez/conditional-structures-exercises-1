# Solicitar al usuario que ingrese un número
number = int(input("Enter a number to display its multiplication table: "))

# Mostrar la tabla de multiplicar del número ingresado
print(f"\nMultiplication table for {number}:\n")
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")