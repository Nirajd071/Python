def sum_positive_numbers(numbers):
    return sum(num for num in numbers if num > 0)
numbers_list = [1, -2, 3, -4, 5, 6]
positive_sum = sum_positive_numbers(numbers_list)
print(f"The sum of positive numbers in the list is: {positive_sum}")
