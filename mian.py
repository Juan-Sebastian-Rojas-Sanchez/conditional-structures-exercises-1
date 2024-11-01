# Set the size of the multiplication table
size = 10

# Print the header
for i in range(1, size + 1):
    print(f"{i:2}", end="  ")
print()  # New line for header

# Print each row of the multiplication table
for i in range(1, size + 1):
    for j in range(1, size + 1):
        print(f"{i * j:2}", end="  ")  # Multiply and format the output
    print()  # New line for the next row