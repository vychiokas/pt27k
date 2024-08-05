import random


def get_random_number():
    return random.randint(0, 10)


def find_sum(num1: int, num2: int, num3: int) -> int:
    sum_nums = num1 + num2 + num3  # Finds the sum of num1 and num2
    return sum_nums  # Returns the sum of the numbers


number = find_sum(1, 2)

print(number)
