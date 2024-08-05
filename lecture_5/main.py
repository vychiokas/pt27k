# squares = []
# for number in range(10):
#     squares.append(number * number)
# print(squares)


# squares = [number * number for number in range(10)]
# print(squares)


# squares = [number * number for number in range(10) if number != 5]
# print(squares)


# squares = [number * number for number in range(10) if number % 2 == 0]
# print(squares)


# names = ["Albert", "Alma", "Joseph", "Zoro"]
# print([name for name in names if name.startswith("A")])


# names = ["Albert", "Alma", "Joseph", "Zoro"]
# print([name for name in names if name.startswith("A") and "e" in name])




# squares = {i: i * i for i in range(10)}
# print(squares)



# values = ["a", "b", "c"]
# index = 0
# value_dict = {}


# for value in values:
#     print(index, value)
#     value_dict[index] = value
#     index += 1

# print(value_dict)



# values = ["a", "b", "c"]
# for index, value in enumerate(values):
#     print(index, value)

import math


print(math.ceil(6.1))

print(math.floor(11.1))
