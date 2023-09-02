#!/bin/env python3
message = "Я люблю своего мужа"
print(message)

message = "Я приготовила ему вкусный ужин"
print(message)

message = "I told my friend, 'Python is my favourite language'"
print(message)

name = "olga"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "olga"
last_name = "moiseyenko"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")
print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")
favorite_language = "python "
favorite_language.rstrip()
name = "Eric"
print(f"Hello {name}, would you like to learn some Python today?")
quote = 'Albert Einstein once said, "A person who never made a mistake never tried anything new."'
print(quote)
famous_person = "Albert Einstein"
message = f"{famous_person} once said, 'A person who never made a mistake never tried anything new.'"
print(message)
name = "\tOlya\t"
print(name)
print(name.strip())
print(4 * 2)
print(12 - 4)
print(5 + 3)
print(16 / 2)

NUMBER = 87
# const - это переменная в Python, значение которой не изменяется.
# Пишется в верхнем регистре.
message = f"{NUMBER} is my favourite number"
print(message)

names = ["Evgen", "Olga", "Elyzaveta", "Victoria", "Leo"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[-1])
message = f"My friend's name is {names[0]}"
print(message)
message = f"My friend's name is {names[1]}"
print(message)
message = f"My friend's name is {names[2]}"
print(message)
message = f"My friend's name is {names[3]}"
print(message)
message = f"My friend's name is {names[4]}"
print(message)

motorcycles = ["honda", "yamaha", "suzuki"]
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

guests = ["Anna", "Victor", "Julia"]
message = f"I invite {guests[0]} to dinner."
print(message)
message = f"I invite {guests[1]} to dinner."
print(message)
message = f"I invite {guests[2]} to dinner."
print(message)
print(guests[2])
guests[2] = "Leo"
print(guests)
message = f"I invite {guests[0]} to dinner."
print(message)
message = f"I invite {guests[1]} to dinner."
print(message)
message = f"I invite {guests[2]} to dinner."
print(message)
message = "I decided to invite more guests"
print(message)
guests = ["Anna", "Victor", "Julia"]
guests.insert(0, "Elyzaveta")
print(guests)
guests.insert(1, "Olya")
print(guests)
guests.append("Evgen")
print(guests)
fav_guest = guests.pop()
print(fav_guest)
print(guests)
guests.pop()
print(guests)
guests.pop()
print(guests)
last_guest = guests.pop()
print(guests)
message = f"Sorry I cann't invite {last_guest} on dinner"
print(message)
del guests[0]
print(guests)
del guests[0]
print(guests)

countries = ["Switzerland", "Norway", "Italy", "France", "England"]
print(countries)
print(sorted(countries))
print(countries)
countries.reverse()
countries.reverse()
countries.sort()
print(countries)
countries.sort(reverse=True)
print(countries)
len(countries)
print(len(countries))
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")


pizzas = ["pepperoni", "bavaria", "napoletana"]
for pizza in pizzas:
    print(f"I like pizza {pizza}!")
print("I really love pizza!")

dogs = ["husky", "colly", "spitz"]
for dog in dogs:
    print(f"A {dog} would make a great pet")
print("Any of these animals would make a great pet")

for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

for value in range(1, 21):
    print(value)

million = list(range(1, 1000001))
print(min(million))
print(max(million))
print(sum(million))

odd_numbers = list(range(1, 20, 2))
print(odd_numbers)

for value in range(1, 20):
    print(value)

numbers = list(range(3, 30, 3))
print(numbers)

for value in range(3, 30, 3):
    print(value)

cube = [value**3 for value in range(1, 11)]
print(cube)

players = ["charles", "martina", "michael", "florence", "eli"]
print("Here are the first three players in my team:")
for player in players[:3]:
    print(player.title())

my_foods = ["pizza", "cake", "salat", "falafel", "carrot cake"]
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

friend_foods = my_foods
my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite food's are:")
print(my_foods)

print("\nMy friend's favorite food's are:")
print(friend_foods)

lists = ["one", "two", "three", "four", "five", "six"]
for list in lists[1:4]:
    print(list)
print("The first three items in the list are:")

pizzas = ["pepperoni", "bavaria", "napoletana"]
friend_pizzas = pizzas[:]
print(friend_pizzas)

friend_pizzas = pizzas
pizzas.append("italia")
friend_pizzas.append("vegan")

print("My favorite pizzas are:")
for pizza in pizzas[0:4]:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas[0:4]:
    print(friend_pizzas)

for pizza in pizzas:
    print(pizza)

dimensions = (200, 50)

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)


menus = ("pizza", "burger", "tea", "coffee", "salad")
for menu in menus:
    print(menu)

menus = ("chicken", "apple", "tea", "coffee", "salad")
for menu in menus:
    print(menu)

car = "subaru"
print("Is car == 'subaru'? I predict True.")
print(car == "subaru")

print("\nIs car == 'audi'? I predict False.")
print(car == "audi")

# alien_color = "green"
# if alien_color == "green":
#     print("You have earned 5 points")


alien_color = "green"
if alien_color == "green":
    print("You have earned 5 points")
elif alien_color == "yellow":
    print("You have earned 10 points")
else:
    alien_color == "red"
    print("You have earned 15 points")

age = 2

if age < 2:
    print("Младенец")
elif age >= 4 or age < 4:
    print("Малыш")
elif age >= 4 or age < 13:
    print("Ребенок")
elif age >= 13 or age < 20:
    print("Подросток")
elif age >= 20 or age < 64:
    print("Взрослый")
else:
    age >= 65
print("Пожилой человек")

favorite_fruits = ("bananas", "strawberry", "apple")
if "bananas" in favorite_fruits:
    print("You really like bananas")
if "strawberry" in favorite_fruits:
    print("You really like strawberry")
if "apple" in favorite_fruits:
    print("You really like apple")
if "pineapple" not in favorite_fruits:
    print("You don't like pineapple")
if "lemon" not in favorite_fruits:
    print("You don't like lemon")

# alien_0 = {"color": "green", "points": "5"}
# new_points = alien_0["points"]
# print(f"You just earned {new_points} points!")

# alien_0 = {"color": "green", "points": "5"}
# alien_0["x_position"] = 0
# alien_0["y_position"] = 25
# print(alien_0)

# alien_0 = {}
# alien_0["color"] = "green"
# alien_0["points"] = 5

# print(alien_0)

# alien_0 = {"color": "green"}
# print(f"The alien is {alien_0['color']}.")

# alien_0["color"] = "yellow"
# print(f"The alien is now {alien_0['color']}.")

alien_0 = {"color": "green", "speed": "slow"}
point_value = alien_0.get("points", "No points value assigned")
print(point_value)

user_0 = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favorite_languages = {"jen": "python", "sarah": "c", "edward": "ruby", "phil": "python"}

friends = ["phil", "sarah"]
for name in favorite_languages.keys():
    print(name.title())

if name in friends:
    language = favorite_languages[name].title()
    print(f"\t{name.title()}, I see you love {language}!")

if "erin" not in favorite_languages.keys():
    print("Erin, please take our poll!")


favorite_languages = {"jen": "python", "sarah": "c", "edward": "ruby", "phil": "python"}
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll!")

print("The following languages have been mentioned")
for language in favorite_languages.values():
    print(language.title())

alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 7}
alien_2 = {"color": "red", "points": 8}
aliens = [alien_0, alien_1, alien_2]

aliens = []

for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
    elif alien["color"] == "yellow":
        alien["color"] = "red"
        alien["speed"] = "fast"
        alien["points"] = 15
print(aliens)

pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"],
}

print(f"You ordered a {pizza['crust']} - crust pizza " "with the following toppings:")

for topping in pizza["toppings"]:
    print("\t" + topping)


message = input("Tell me something, and I will repeat it back to you!")
print(message)

prompt = "If you tell us who you are, we can personalize messages you see"
prompt += "\nWhat is your first name?"
name = input(prompt)
print(f"\nHello, {name}!")

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program"
message = ""
while message != "quit":
    message = input(prompt)
    print(message)

prompt = "\nSelect pizza ingredients, and I will add them to your order."
prompt += "\nEnter 'quit' to end the program"
message = ""
while message != "quit":
    message = input(prompt)
    print(message)
    print("Ingredients are added to your order")


age = 2

if age < 3:
    print("Билет бесплатно")
elif age >= 3 or age < 12:
    print("Цена билета 10$")
elif age >= 12:
    print("Цена билета 15$")

message = input("If you tell us how old are you, we can told you a price of a ticket")
print(message)

unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
