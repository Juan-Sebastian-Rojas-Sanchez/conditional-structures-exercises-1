#Escriba un programa que entregue la edad del usuario a partir de su fecha de nacimiento:

#Ingrese su fecha de nacimiento.
#Dia: 14
#Mes: 6
#Anno: 1948
#Usted tiene 62 annos
#Por supuesto, el resultado entregado depende del día en que su programa será ejecutado.

#Para obtener la fecha actual, puede hacerlo usando la función localtime que viene en el módulo time. Los valores se obtienen de la siguiente manera (suponiendo que hoy es 11 de marzo de 2011):

#>>> from time import localtime
#>>> t = localtime()
#>>> t.tm_mday
#11
#>>> t.tm_mon
#3
#>>> t.tm_year
#2011
#El programa debe tener en cuen#ta si el cumpleaños ingresado ya pasó durante este año, o si todavía no ocu
# rre
# .
from time import localtime

t = localtime()
day_current = t.tm_mday
month_current = t.tm_mon
year_current = t.tm_year

day_birth = int(input("Enter your birth date.\nDay: "))
month_birth = int(input("Month: "))
year_birth = int(input("Year: "))

age = year_current - year_birth

if (month_birth > month_current) or (month_birth == month_current and day_birth > day_current):
    age -= 1

print(f"You are {age} years old.")
