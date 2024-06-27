#!/usr/bin/env python3
# User class will contain first_name, last_name, email, phone-number
class User:
    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
    
#create getter function
        @property
        def get_first_name(self):
            return self.__first_name
        
        def get_last_name(self):
            return self.__last_name
        
        def get_email(self):
            return self.__email
        
        def get_phone_number(self):
            return self.__phone_number

    def describe_user(self):
        print("User 1 information: \t\n\n")
        print("First name: \t\t{}\n".format(self.__first_name))
        print("Last name: \t\t{}\n".format(self.__last_name))
        print("email: \t\t{}\n".format(self.__email))
        print("Phone number: \t\t{}\n".format(self.__phone_number))
    
    def greet_user(self):
        print(f"Hello, {self.__first_name} {self.__last_name}!")

def main():
    Eze = User()

    first_name = input("Enter First Name here")
    last_name = input("Enter Last Name here")
    email = input("Enter Email here")
    phone_number = input("Enter Phone Number here")

    Eze.describe_user()
    Eze.greet_user()