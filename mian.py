#Escriba un programa que simule una calculadora básica, este puede realizar operación de suma, resta, multiplicación y división.

#El programa debe recibir como entrada 2 números reales y un operador, que puede ser +, -, * o /.

#La salida del programa debe ser el resultado de la operación.#

#Operando: 3
#Operador: +
#Operando: 2
#3 + 2 = 5
#Operando: 6
#Operador: -
#Operando: 7
#6 - 7 = -1
#Operando: 4
#Operador: *
#Operando: 5
#4 * 5 = 20
#Operando: 10
#Operador: /
#Operando: 4
#10 / 4 = 2.5
#Operando: -1
#Operador: **
#Operando: 4
#-1 ** 4 = 1

operator1 = float(input("Operando 1: "))
operator2 = float(input("Operando 2: "))
operatoR = input("Operador (+, -, *, /, **): ")

result = None

if operatoR == '+':
    result = operator1 + operator2
    print(f"{operator1} + {operator2} = {result}")
elif operatoR == '-':
    result = operator1 - operator2
    print(f"{operator1} - {operator2} = {result}")
elif operatoR == '*':
    result = operator1 * operator2
    print(f"{operator1} * {operator2} = {result}")
elif operatoR == '/':
    if operator2 != 0:
        result = operator1 / operator2
        print(f"{operator1} / {operator2} = {result}")
    else:
        print("Error: No se puede dividir por cero.")
elif operatoR == '**':
    result = operator1 ** operator2
    print(f"{operator1} ** {operator2} = {result}")
else:
    print("Error: Operador no válido. Por favor, utiliza +, -, *, / o **.")
