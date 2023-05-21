def print_divisible_numbers(start, end, divisor):
    divisible_numbers = []
    for num in range(start, end+1):
        if num % divisor == 0:
            divisible_numbers.append(num)
    return divisible_numbers

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))
divisor = int(input("Enter the divisor: "))

numbers = print_divisible_numbers(start_range, end_range, divisor)
print("Numbers divisible by", divisor, "in the range", start_range, "to", end_range, "are:")
print(numbers)
