#Escriba un programa que reciba como entrada dos números, y los muestre ordenados de menor a mayor:

#Ingrese numero: 51
#Ingrese numero: 24
#24 51
#A continuación, escriba otro programa que haga lo mismo con tres números:

#Ingrese numero: 8
#Ingrese numero: 1
#Ingrese numero: 4
#1 4 8
#Finalmente, escriba un tercer programa que ordene cuatro números:

#Ingrese numero: 7
#Ingrese numero: 0
#Ingrese numero: 6
#Ingrese numero: 1
#0 1 6 7
#
#Hay más de una manera de resolver cada ejercicio.

number1 = int(input("Enter number: "))
number2 = int(input("Enter number: "))
number3 = int(input("Enter number: "))
number4 = int(input("Enter number: "))

numbers = [number1, number2, number3, number4]

numbers.sort()
print(*numbers)