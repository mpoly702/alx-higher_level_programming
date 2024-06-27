#!/usr/bin/env python3

"""this code is a practise code on how to create classes"""

class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(f"the name of this restaurant is {self.name}")
        print(f"We specialize in {self.cuisine}")

    def open_restaurant(self):
        print(f"We @ {self.name} are ready to offer you 24/7 services")

restaurant = Restaurant("Bukkateria", "Intercontinental")
print(f"{restaurant.name} is the best in Lagos, specializing in delivering {restaurant.cuisine} dishes")

restaurant.describe_restaurant()
restaurant.open_restaurant()

Sizzlers  = Restaurant("Sizzlers", "Intercontinental")
Sizzlers.describe_restaurant()
Chicken_republic = Restaurant("Chicken_republic", "Fried Chickens")
Chicken_republic.describe_restaurant()