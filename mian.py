print ("Exercise 10 TRIANGLES")

t1 = float(input("Insert A: "))
t2 = float(input("Insert B: "))
t3 = float(input("Insert C: "))

if t1 + t2 > t3 and t1 + t3 > t2 and t2 + t3 > t1:
    if  t1 == t2 == t3:
        print ("El triangulo equilatero")
    elif t1 == t2 or t1 == t3 or t2 == t3:
        print ("El triangulo isosceles")
    else:
        print ("El triangulo es escaleno")
else:
    print ("No es un triangulo valido")