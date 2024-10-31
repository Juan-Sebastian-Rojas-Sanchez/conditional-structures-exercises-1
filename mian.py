print ("Exercise 9 TENNIS SET")

p1 = int(input("games won by A: "))
p2 = int(input("games won by B: "))

#Conocer si es invalido
if p1 > 7 or p2 > 7 or ( p1==7 and p2 < 5) or (p2==7 and p1 < 5) or abs(p1-p2) > 2:
    print ("Invalid")
#Conocer si aun no finaliza
elif (p1 <= 6 and p2 <= 6 ) or (p1==6 and p2==6):
    print ("It's not over yet")
#Conocer si gana P1
elif (p1 == 6 and p2 <= 4) or (p1 == 7 and p2 == 5) or (p1 == 7 and p2 == 6):
    print ("Won A")

elif (p2 == 6 and p1 <= 4) or (p2 == 7 and p1 == 5) or (p2 == 7 and p1 == 6):
    print ("Won B")