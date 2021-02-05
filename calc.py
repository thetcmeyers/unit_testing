def add(a,b):
    return (a + b)

def sub(a,b):
    return (a - b)

def mul(a,b):
    return (a * b)

def div(a,b):
    if b == 0:
        print("Error, cannot divide by 0")
        return
    return (a / b)

## Input Cases
print("Welcome to the calculator app!")
print()


i = True
while i:
    x = True
    while x:
        a = int(input("Enter your first number: "))
        # Testing to make sure we received the right input
        print("Input recieved: ", a)
        # giving the user a chance to edit
        z = input("Is this your number (y/n): ")
        if(z == "y"):
            x = False

    y = True
    while y:
        b = int(input("Enter your first number: "))
        # Testing to make sure we received the right input\
        print("Input received: ", b)
        # giving the user a chance to edit
        z = input("Is this your number (y/n): ")
        if(z == "y"):
            y = False

    print("What would you like to do?")
    print("Press 1 for addition")
    print("Press 2 for subtraction")
    print("Press 3 for multiplication")
    print("Press 4 for division")
    print("Press 5 to quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Adding %s + %s" % (a , b))
        c = add(a,b)
        print("Output: ", c)


    if choice == 2:
        print("Subtracting %s - %s" % (a , b))
        c = sub(a,b)
        print("Output: ", c)

    if choice == 3:
        print("Adding %s * %s" % (a , b))
        c = mul(a,b)
        print("Output: ", c)

    if choice == 4:
        print("Adding %s / %s" % (a , b))
        c = div(a,b)
        print("Output: ", c)

    if choice == 5:
        print("Thanks for coming!")
        i = False

    print()
