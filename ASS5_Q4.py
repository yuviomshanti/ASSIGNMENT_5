def print_pattern(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print()
    for i in range(n - 1, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

# Example 
rows = int(input("Enter the number of rows: "))
print_pattern(rows)
