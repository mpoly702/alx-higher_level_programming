#!/usr/bin/env python3

user = {"Name": "Godfrey", 'email': 'godfreyoriaz@gmail.com', 'password': 'Billz@3455'}
#convert this dictionary to  json file

user_info = {}

def login(info: dict = None) -> dict:
    if info is None:
        data = request.get(file.json)
        for key, value in user:
            if value == "Godfrey" and value == 'Billz@3455':
                user_info.update(user)
    
    return user_info


def delete(self, new: dict = None) -> None:
    try:
        if new is not None:
            del new['password']
    except:
        print("Error deleting password")


