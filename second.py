#!/bin/env python3
# print("Hello")

# message = input("If you tell us how old are you, we can told you a price of a ticket")
# print(message)

# unconfirmed_users = ["alice", "brian", "candace"]
# confirmed_users = []

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)

# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())


# responses = {}

# polling_active = True
# while polling_active:
#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb someday? ")

# responses[name] = response
# repeat = input("Would you like to let another person to respond? (yes/no)")
# if repeat == "no":
#     polling_active = False

# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(f"{name} would like to climb {response}.")


sandwich_orders = ["Ham and cheese", "Roast beef", "Corned beef", "BLT"]
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()

    print(f"I made your {current_order}")
    finished_sandwiches.append(current_order)
print("\n These sandwiches were made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())


# Functions
def display_message():
    print("Functions in Python")


display_message()


def favorite_book(title):
    print(f"One of my favorite books is {title}")


favorite_book("Alice in Wonderland")


# def make_shirt(size, label):
#     print(f"I have a t-shirt")
#     print(f"My t-shirt has {size} and a text {label}")
# make_shirt("x-size", "I love python")


def make_shirt(size="L", label="I love Python"):
    print(f"I have a t-shirt")
    print(f"My t-shirt has {size} size and a text {label}")


make_shirt("S", "I love JavaScript")


def describe_city(city, country="Iceland"):
    print(f"{city} is in {country}")


describe_city("Reykjavik")


def make_album(name_singer, name_alb, songs=None):
    album = {"name": name_singer, "alb": name_alb}
    if songs:
        album["songs"] = songs
    return album


musician = make_album("Monatik", "Run")
print(musician)
musician = make_album("Adele", "Home")
print(musician)
musician = make_album("Ed Sheran", "Shape of you")
print(musician)
musician = make_album("Ed Sheran", "Be my love", songs=12)
print(musician)


# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()


# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")

#     f_name = input("First name:")
#     if f_name == "q":
#         break

#     l_name = input("Last name: ")
#     if l_name == "q":
#         break

#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")

# while True:
#     print("\nPlease tell me your favorite album:")
#     print("(enter 'q' at any time to quit)")

#     name_singer = input("Name singer: ")
#     if name_singer == "q":
#         break

#     name_alb = input("Name album: ")
#     if name_alb == "q":
#         break

#     album = make_album(name_singer, name_alb)
#     print(f"My favorite album is {album}")


def greet_messages(messages):
    for message in messages:
        msg = f"If you meet a friend say {message}"
        print(msg)


messages = ["Hi", "Hello", "Good morning"]
greet_messages(messages)

# unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
# completed_models = []


def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


def send_messages(greet_messages, sent_messages):
    while greet_messages:
        current_message = greet_messages.pop()
        print(f"Greet message: {current_message}")
        sent_messages.append(current_message)


def show_sent_messages(sent_messages):
    print("\n This messages were printed:")
    for sent_message in sent_messages:
        print(sent_message)


greet_messages = ["Hi", "Hello", "Good morning"]
sent_messages = []

send_messages(greet_messages[:], sent_messages)
print(greet_messages)
print(sent_messages)
show_sent_messages(sent_messages)
