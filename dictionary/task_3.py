#!/bin/env python
# Создайте словарь с названием рек и стран, по которой
# протекает каждая река.
# Используйте цикл for для вывода сообщения с упоминанием реки
# и страны. Например "The Dnepr runs
# through Ukraine."
# Используйте цикл для вывода названия каждой реки.
# Используйте цикл для вывода названия каждой страны.

geography_data = {
    "nile": "egypt",
    "neva": "russia",
    "volga": "russia",
}

for river, country in geography_data.items():
    print(f"The {river.title()} runs through {country.title()}.")

for river in geography_data.keys():
    print(river.title())

for country in geography_data.values():
    print(country.title())
