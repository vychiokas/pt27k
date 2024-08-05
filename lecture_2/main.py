# user_info = {
# 	"name": "Albert",
# 	"surname": "Einstein",
# 	"occupation": {
# 		"role": "Professor",
# 		"workplace": "University of Berlin"
# 	},
#     "languages": ["German", "Latin", "Italian", "English", "French"]
# }


# # for language in user_info["languages"]:
# #     print(language)

# print("asd" in user_info["languages"])



# d = {'a': 10, 'b': 20, 'c': 30}

# for value in d.values():
#     print(f"value is: {value}")


# d = {'a': 10, 'b': 20, 'c': 30}

# result = d.pop('a')
# print(result)
# print(d)


# dict_one = {'a': 10, 'b': 20, 'c': 30}
# dict_two = {'b': 200, 'd': 400}


# dict_one.update(dict_two)
# print(dict_one)



# test_keys = ["Albert", "Tom", "Stephen"]
# test_values = [1, 4, 5]


# my_dictionary= dict(zip(test_keys, test_values))
# print(my_dictionary)


numbers_list = [1, 2, 3, 4, 5, 5, 5, 6]

numbers_set = set(numbers_list)
print(len(numbers_set))