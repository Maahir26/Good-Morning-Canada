TAXPERCENTAGE = 0.13
cost = 0
customerOrder = ""
quantity = 0

#Cost of each item on the menu
eggs_cost = 0.99
bacon_cost = 0.49
sausage_cost = 1.49
hash_brown_cost = 1.19
toast_cost = 0.79
coffee_cost = 1.49
tea_cost = 1.09


def formatInput(textLine):
    textLine = textLine.lower().strip()
    wordList = textLine.split()
    textLine = "".join(wordList)
    return textLine


# small breakfast includes 1egg, 1hash brown, 2toasts, 1 bacon, 1 sausage
smallbreakfast_price = eggs_cost * 1 + hash_brown_cost * 1 + toast_cost * 2 + bacon_cost * 2 + sausage_cost * 1
# regular breakfast includes 2eggs, 1hash brown, 2toasts, 4bacon, 2sausages
regularbreakfast_price = eggs_cost * 2 + hash_brown_cost * 1 + toast_cost * 2 + bacon_cost * 4 + sausage_cost * 2
# big breakfast includes 3 eggs, 2hash brown, 4toasts, 6bacon, 3sausages
bigbreakfast_price = eggs_cost * 3 + hash_brown_cost * 2 + toast_cost * 4 + bacon_cost * 6 + sausage_cost * 3


while customerOrder != "q":
    customerOrder = input(
        "Enter item(q to terminate): small breakfast, regular breakfast, big breakfast, egg, bacon, sausage, hash brown, toast, coffee, tea:")
    customerOrder = formatInput(customerOrder)
    quantity = ""

    if 'smallbreakfast' in formatInput(customerOrder):
        quantity = input("Enter quantity:")
        while not quantity.isnumeric():
            print("The input you entered is invalid")
        cost = cost + int(quantity) * smallbreakfast_price

    elif 'regularbreakfast' in formatInput(customerOrder):
        quantity = input("Enter quantity:")
        while not quantity.isnumeric():
            print("The input you entered is invalid")
        cost = cost + int(quantity) * regularbreakfast_price

    elif 'bigbreakfast' in formatInput(customerOrder):
        quantity = input("Enter quantity:")
        while not quantity.isnumeric():
            print("The input you entered is invalid")
        cost = cost + int(quantity) * bigbreakfast_price

    elif 'egg' in formatInput(customerOrder):
        quantity = input("Enter quantity:")
        while not quantity.isnumeric():
            print("The input you entered is invalid")
        cost = cost + int(quantity) * eggs_cost

    elif 'bacon' in formatInput(customerOrder):
        quantity = input("Enter quantity:")
        while not quantity.isnumeric():
            print("The input you entered is invalid")
        cost = cost + int(quantity) * bacon_cost

    elif 'sausage' in formatInput(customerOrder):
        quantity = input("Enter quantity:")
        while not quantity.isnumeric():
            print("The input you entered is invalid")
        cost = cost + int(quantity) * sausage_cost

    elif 'hashbrown' in formatInput(customerOrder):
        quantity = input("Enter quantity:")
        while not quantity.isnumeric():
            print("The input you entered is invalid")
        cost = cost + int(quantity) * hash_brown_cost

    elif 'toast' in formatInput(customerOrder):
        quantity = input("Enter quantity:")
        while not quantity.isnumeric():
            print("The input you entered is invalid")
        cost = cost + int(quantity) * toast_cost

    elif 'coffee' in formatInput(customerOrder):
        quantity = input("Enter quantity:")
        while not quantity.isnumeric():
            print("The input you entered is invalid")
        cost = cost + int(quantity) * coffee_cost

    elif 'tea' in formatInput(customerOrder):
        quantity = input("Enter quantity:")
        while not quantity.isnumeric():
            print("The input you entered is invalid")
        cost = cost + int(quantity) * tea_cost

        # When the user inputs "q" it will print the total before tax, the tax, and then the total after tax and then break out the loop
    elif customerOrder == "q":
        taxonorder = cost * TAXPERCENTAGE
        print("Cost:  ${0:.2f}".format(cost))
        print("Tax:   ${0:.2f}".format(taxonorder))
        print("Total: ${0:.2f}".format(cost + taxonorder))


    else:
        print("not valid input")
