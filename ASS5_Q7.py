def find_multiples():
    multiples = []
    for num in range(1, 501):
        if num % 7 == 0 and num % 11 == 0:
            multiples.append(num)
    return multiples

# Example usage
result = find_multiples()
print("Numbers that are multiples of 7 and divisible by 11 in the range 1-500 are:")
print(result)
