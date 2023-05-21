def print_alphabet_triangle(rows):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_index = 0

    for i in range(1, rows+1):
        for j in range(i):
            print(alphabet[alphabet_index], end='')
            alphabet_index = (alphabet_index + 1) % len(alphabet)
        print()

# Example usage
num_rows = int(input("Enter the number of rows: "))
print_alphabet_triangle(num_rows)
