#Escriba un programa que determine si un caracter ingresado es letra, número, o ninguno de los dos. En caso que sea letra, determine si es mayúscula o minúscula.

#Ingrese caracter: 9
#Es numero.
#Ingrese caracter: A
#Es letra mayúscula.
#Ingrese caracter: f
#Es letra minúscula.
#Ingrese caracter: #
#No es letra ni número.

character = input("Ingrese carácter: ")

if character.isalpha():
    if character.isupper():
        print("It is a capital letter.")
    else:
        print("It is a lowercase letter.")
# Check if the character is a number
elif character.isdigit():
    print("It's a number.")
# If it is not a letter or number
else:
    print("Not a letter or number.")