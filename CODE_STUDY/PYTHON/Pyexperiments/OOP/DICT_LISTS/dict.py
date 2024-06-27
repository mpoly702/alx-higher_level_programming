#!/usr/bin/env python3
"""
this script helps me practise dictionaries
"""

#creating a dictionary object
dicto = dict()
#creating an empty dictionary
dicto = {}
#print the dictionary
print(dicto)
#populating the dicto dictionary
dicto = {"Name": "Godfrey Oriazowan", "email": "godfreyoriaz@gmail.com", "Username": "mpoly702", "Password": "Billionair@12"}
username, password = dicto["Username"], dicto["Password"]
print(username, password)
Email = dicto.get("email")
Name = dicto.get("Name")
print(Email, Name)