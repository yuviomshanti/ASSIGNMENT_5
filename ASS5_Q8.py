def analyze_numbers(numbers):
    positive_nums = []
    negative_nums = []
    odd_nums = []
    even_nums = []
    num_counts = {}

    for num in numbers:
        # Categorize numbers into positive, negative, odd, or even
        if num > 0:
            positive_nums.append(num)
        elif num < 0:
            negative_nums.append(num)

        if num % 2 == 0:
            even_nums.append(num)
        else:
            odd_nums.append(num)

        # Count the occurrences of each number
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1

    return positive_nums, negative_nums, odd_nums, even_nums, num_counts

# Example usage
user_input = input("Enter 10 integer values (space-separated): ")
numbers = list(map(int, user_input.split()))

positive_nums, negative_nums, odd_nums, even_nums, num_counts = analyze_numbers(numbers)

print("Positive numbers:", positive_nums)
print("Negative numbers:", negative_nums)
print("Odd numbers:", odd_nums)
print("Even numbers:", even_nums)
print("Number of occurrences of each number:", num_counts)
