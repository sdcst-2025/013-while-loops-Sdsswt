#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:

username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied

example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 12345
Access granted


"""

login = True

while login:
    x = input("enter your username ")
    y = input("enter your password ")
    x = str(x)
    y = str(y)
    if x != "admin" and y != "12345":
        print("access denied")
    else:
        login = False
        print("access granted")