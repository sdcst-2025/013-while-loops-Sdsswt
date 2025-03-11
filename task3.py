#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

"""

number = True

while number:
    x = input("enter a number ")
    x = float(x)
    if x % 2 == 0:
        print("number is an even integer")
        exit()
    else:
        print("number is not an even iteger")