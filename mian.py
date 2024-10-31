print ("Exercise 11 Body mass index")

stature  = float(input("Insert stature: "))
Weight   = float(input("Insert weight: "))
age      = float(input("Insert age: "))

imc  = Weight / (stature**2)

if age < 45:
    if imc < 22.0:
        risk = "low"
    else:
        risk = "medium"
else:
    if imc < 22.0:
        risk = "medium"
    else:
        risk = "high"

print(f"Your risk of coronary heart disease is {risk}.")