#Suma entre números
# Get user input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Ensure num1 is less than num2
if num1 > num2:
    num1, num2 = num2, num1

# Calculate the sum of numbers between num1 and num2
total_sum = sum(range(num1 + 1, num2))

# Print the result
print(f"The sum is {total_sum}")