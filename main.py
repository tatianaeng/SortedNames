# Write a program that asks the user to enter 3 names and then displays the names sorted in ascending order.
# For example, if the user enters "Charlie", "Leslie", and "Andy", the program would display...
# Andy, Charlie, Leslie

# ask the user to enter 3 names
name_1 = input("Please enter 3 names.\nName 1: ").lower()
name_2 = input("Name 2: ").lower()
name_3 = input("Name 3: ").lower()

print("\nThanks! Here are the names in alphabetical order:")

# if name_1 comes before name_2 alphabetically, we will say name_1 < name_2.
# the following decision structures will help us print the names in alphabetical order.

#assume name_1 comes first alphabetically
if (name_1 < name_2 and name_1 < name_3):
    print(name_1)
    if (name_2 < name_3):
        print(name_2)
        print(name_3)
    else:
        print(name_3)
        print(name_2)

#assume name_2 comes first alphabetically    
if (name_2 < name_1 and name_2 < name_3):
    print(name_2)
    if (name_1 < name_3):
        print(name_1)
        print(name_3)
    else:
        print(name_3)
        print(name_1)

#assume name_3 comes first alphabetically    
if (name_3 < name_1 and name_3 < name_2):
    print(name_3)
    if (name_2 < name_1):
        print(name_2)
        print(name_1)
    else:
        print(name_1)
        print(name_2)