#!/usr/bin/env python3
#number dictionary
num_dict = {
    1: 24, 
    2: 28,
    3: 45,
    4: 52,
    5: 71
}
print(num_dict)
print(num_dict[1])
num_dict[6] = 34
for key, value in num_dict.items():
    print(f"{key}: {value}")

#print just the keys
for key in num_dict.keys():
    print(key)
for value in num_dict.values():
    print(value)
print(f"\n\n")
print(num_dict[2])
print(num_dict[3])
print(num_dict[4])
print(f"\n\n")

if 33 in num_dict:
    print(" 33:Number available")
else:
    print("33: Number UNAVAILABLE")