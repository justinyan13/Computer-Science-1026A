# Justin Yan
# jyan388
# 251150279

def format_input(text_line):
    text_line = text_line.lower().strip()
    word_list = text_line.split()
    text_line = " ".join(word_list)
    return text_line


# setting item pricing
egg = 0.99
bacon = 0.49
sausage = 1.49
hash_brown = 1.19
toast = 0.79
coffee = 1.49
tea = 1.09

# setting meal pricing
small_breakfast = egg + hash_brown + (2 * toast) + (2 * bacon) + sausage
regular_breakfast = (2 * egg) + hash_brown + (2 * toast) + (4 * bacon) + (2 * sausage)
big_breakfast = (3 * egg) + (2 * hash_brown) + (4 * toast) + (6 * bacon) + (3 * sausage)

# establishing while loop variables
item = ''
quantity = ''
cost = 0

# instructions
# prompt user for input
# while loop that terminates when user enters q
# accept input non-case sensitive
# if invalid item input; display error message, re prompting user for input
# use quantity.isnumeric() to check quantity input, re prompt if invalid
# compute cost (2 decimal float)
# compute 13% tax (2 decimal float)
# compute total price (2 decimal float)


# create an if statement for each option
# add input cost * quantity to cost variable
# output sum if input is q
while item != 'q':
    item = format_input(input(
        "Enter item (q to terminate): small breakfast, regular breakfast, big breakfast, egg, bacon, sausage, hash brown, toast, coffee, tea: "))

    if item == 'small breakfast':
        quantity = input("Enter quantity :")
        while not quantity.isnumeric():
            print("Invalid input, please re-enter quantity")
            quantity = input("Enter quantity :")
        quantity = int(quantity)
        cost += small_breakfast * quantity
    elif item == 'regular breakfast':
        quantity = input("Enter quantity :")
        while not quantity.isnumeric():
            print("Invalid input, please re-enter quantity")
            quantity = input("Enter quantity :")
        quantity = int(quantity)
        cost += regular_breakfast * quantity
    elif item == 'big breakfast':
        quantity = input("Enter quantity :")
        while not quantity.isnumeric():
            print("Invalid input, please re-enter quantity")
            quantity = input("Enter quantity :")
        quantity = int(quantity)
        cost += big_breakfast * quantity
    elif item == 'egg':
        quantity = input("Enter quantity :")
        while not quantity.isnumeric():
            print("Invalid input, please re-enter quantity")
            quantity = input("Enter quantity :")
        quantity = int(quantity)
        cost += egg * quantity
    elif item == 'bacon':
        quantity = input("Enter quantity :")
        while not quantity.isnumeric():
            print("Invalid input, please re-enter quantity")
            quantity = input("Enter quantity :")
        quantity = int(quantity)
        cost += bacon * quantity
    elif item == 'sausage':
        quantity = input("Enter quantity :")
        while not quantity.isnumeric():
            print("Invalid input, please re-enter quantity")
            quantity = input("Enter quantity :")
        quantity = int(quantity)
        cost += sausage * quantity
    elif item == 'hash brown':
        quantity = input("Enter quantity :")
        while not quantity.isnumeric():
            print("Invalid input, please re-enter quantity")
            quantity = input("Enter quantity :")
        quantity = int(quantity)
        cost += hash_brown * quantity
    elif item == 'toast':
        quantity = input("Enter quantity :")
        while not quantity.isnumeric():
            print("Invalid input, please re-enter quantity")
            quantity = input("Enter quantity :")
        quantity = int(quantity)
        cost += toast * quantity
    elif item == 'coffee':
        quantity = input("Enter quantity :")
        while not quantity.isnumeric():
            print("Invalid input, please re-enter quantity")
            quantity = input("Enter quantity :")
        quantity = int(quantity)
        cost += coffee * quantity
    elif item == 'tea':
        quantity = input("Enter quantity :")
        while not quantity.isnumeric():
            print("Invalid input, please re-enter quantity")
            quantity = input("Enter quantity :")
        quantity = int(quantity)
        cost += tea * quantity
    elif item == 'q':
        print("\nCost :    ${:.2f}".format(cost))
        print("Tax :    ${:.2f}".format(0.13 * cost))
        print("Total :    ${:.2f}".format(cost * 1.13))
    else:
        print("Error, please enter a new item")
