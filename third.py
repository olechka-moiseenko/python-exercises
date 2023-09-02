#!/bin/env python3


class Dog:
    def __init__(self, name, age):
        # Инициализирует атрибуты name и age
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")


my_dog = Dog("Willie", 6)
your_dog = Dog("Lucy", 3)

print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years age.")
my_dog.sit()
my_dog.roll_over()

print(f"My dog's name is {your_dog.name}")
print(f"My dog is {your_dog.age} years age.")
your_dog.sit()


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The name of a restaurant is {self.restaurant_name}")
        print(f"The type is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is opening now!")

    def check_number_served(self):
        print(f"Restaurant has {self.number_served} orders")

    def set_number_served(self, orders):
        if orders >= self.number_served:
            self.number_served = orders
        else:
            print("Number of orders doesn't changed")

    def increment_number_served(self, clients):
        self.number_served += clients


restaurant = Restaurant("Juger", "georgian")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.set_number_served(20)
restaurant.check_number_served()

restaurant.increment_number_served(15)
restaurant.check_number_served()


class Car:
    def __init__(self, make, model, year):
        # Инициализирует атрибуты описания автомобиля
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        # Возвращает аккуратно отформатированное описание
        long_name = f"{self.year} {self.model} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_used_car = Car("subaru", "outback", 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
