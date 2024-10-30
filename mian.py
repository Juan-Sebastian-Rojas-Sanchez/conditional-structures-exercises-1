#División
#Escriba un programa que pida dos números enteros y que calcule la división, indicando si la división es exacta o no.

#Dividendo: 14
#Divisor: 5

#La división no es exacta.
#Cociente: 2
#Resto: 4
#Dividendo: 100
#Divisor: 10

#La división es exacta.
#Cociente: 10
#Resto: 0

dividing= int(input("dividing: "))
divider= int(input("divider: "))

cociente= dividing//divider
resto= dividing%divider

if resto==0:
    print("The division is exact:")
else:
    print("The division is not exact:")

print(f"Cociente:", {cociente})
print(f"Resto:", {resto})