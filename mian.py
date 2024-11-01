#Potencias de dos
# Get user input
num = int(input("Enter a number: "))

# Generate powers of 2
powers_of_two = [2 ** i for i in range(num + 1)]

# Print the results
print(" ".join(map(str, powers_of_two)))
