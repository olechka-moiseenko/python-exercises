#!/bin/env python
# Создайте словарь с любимыми числами своих друзей
#  и выведите в консоль с помощью цикла for значения
# всех пар ключ-значения.
# Выведите значения всех ключей.

favorite_numbers = {
    "jen": "12",
    "sarah": "24",
    "edward": "7",
    "phil": "14",
}

for name, number in favorite_numbers.items():
    print(f"'{name}': '{number}'")

for key in favorite_numbers:
    print(key)
