#!/usr/bin/env python3
#this script creates instances of a car class and uses a Driver object to drive a car object

class Car:
    def __init__(self, model, year, is_manual=False, max_passengers=10, speed=0.0, rotation=0.0):
        self.model = model
        self.year = year
        self.is_manual = is_manual
        self.max_passengers = max_passengers
        self.speed = speed
        self.rotation = rotation
    
    def accelerate(self, rate: float):
        if rate > 0.0:
            print("The {} is on the move".format(self.model))
        else:
            print("This car is stationary")

    def  brake(self):
        print("The {} has stopped".format(self.model))
        
    def turn(self, direction: str):
        print("The {} is turning {}".format(self.model, direction))

class Driver:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def drive(self, car: Car):
        car.accelerate(1.0)
        car.turn('left')
        car.brake()

luxury_car = Car('Bentley s300', 2000)
my_driver = Driver('flippant Jonas', 'Toyota')
print("{} of {} is mounting {}".format(my_driver.name, my_driver.id, luxury_car.model))
my_driver.drive(luxury_car)
