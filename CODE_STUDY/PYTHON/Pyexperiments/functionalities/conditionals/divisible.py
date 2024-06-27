#!/usr/bin/env python3
def divisible(x: int = None) -> str:
    nl = []
    if x is None:
        User_input = input("Please enter an Integer")
        try:
                x = int(User_input)
                nl.append(x)
        except ValueError:
            return "Please enter a valid integer"
        while len(nl) < 5:
            User_input = input()
            try:
                x = int(User_input)
                nl.append(x)
            except ValueError:
                return "Please enter a valid integer"
    else:
        raise ValueError('Please dont input any parameter')

    xx = []
    # Iterate through numbers from 1500 to 2700 (inclusive)
    for i in range(len(nl)):
        # Check if the number is divisible by 7 and 5 without any remainder
        if (nl[i] % 7 == 0) or (nl[i] % 5 == 0):
        # If the conditions are met, convert the number to a string and append it to the list
            xx.append(str(nl[i]))
        # Join the numbers in the list with a comma and print the result
    print(xx)

if __name__ == '__main__':
    divisible()
