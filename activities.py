def guessing_game():
    number = input("Pick a number: ")
    number = int(number)
    if number < 1 or number > 10:
        raise ValueError("Invalid guess!")
    print("You picked:", number)
    
try:
    x_input = input("Enter x: ")
    y_input = input("Enter y: ")
    x = int(x_input)
    y = int(y_input)
    print("x / y =", (x/y))

except ValueError:
    print("Invalid number entered.")
except ArithmeticError:
    print("Cant divide by 0.")