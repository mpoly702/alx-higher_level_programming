The range function in Python is a versatile built-in function used to generate a sequence of numbers. It's commonly used in for-loops and other scenarios where a sequence of numbers is needed. Here's a more detailed explanation of its usage and functionality:

Basic Syntax
The range function can be called in three different ways:

1.  Single Argument: range(stop)

range(stop)

Generates numbers from 0 to stop - 1.
Example:

for i in range(5):
    print(i)

Output
0
1
2
3
4

2. Two Arguments: range(start, stop)

range(start, stop)
Generates numbers from start to stop - 1.

Example:
for i in range(2, 5):
    print(i)

OUTPUT:
2
3
4

3. Three Arguments: range(start, stop, step)

range(start, stop, step)

Generates numbers from start to stop - 1, incrementing by step.
If step is negative, it decrements from start to stop + 1.

Example:

for i in range(2, 10, 2):
    print(i)

OUTPUT:
2
4
6
8

Understanding the Arguments
start (optional): The beginning of the sequence. If omitted, the sequence starts at 0.
stop: The end of the sequence (exclusive). The sequence stops before stop.
step (optional): The increment (or decrement) between each number in the sequence. If omitted, it defaults to 1.

Example Usages

1. Counting Up:
for i in range(5):
    print(i)

OUTPUT:
0, 1, 2, 3, 4

2.  Counting Down:
for i in range(5, 0, -1):

OUTPUT:
5, 4, 3, 2, 1

3.  Custom Step:
for i in range(1, 10, 2):
    print(i)

OUTPUT:
1, 3, 5, 7, 9

Negative Step:
for i in range(10, 0, -2):
    print(i)

OUTPUT:
10, 8, 6, 4, 2


