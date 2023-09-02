#!/bin/env python
# Создайте словарь с информацией о известном человеке
# (имя, фамилия, возраст, город).
# Выведите все пары "ключ-значения".

my_husband = {
    "first_name": "Evgen",
    "last_name": "Moiseenko",
    "age": "38",
    "city": "Saint-Petersburg",
}
for key in my_husband:
    print(f"~ '{key}': '{my_husband[key]}'")


def printItem(arr, key):
    print(f"'{key}': '{arr[key]}'")


printItem(my_husband, "first_name")
printItem(my_husband, "last_name")


# husband = my_husband["first_name"].title()
print(f"first_name: {my_husband['first_name']}.")

# husband = my_husband["last_name"].title()
print(f"last_name: {my_husband['last_name']}")

# husband = my_husband["age"]
print(f"age: {my_husband['age']}")

# husband = my_husband["city"]
print(f"The city is {my_husband['city']}")
