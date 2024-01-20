def variables():
    ageMonths = "225 months"
    daysYear = "365 days"
    firstPet ="Haroon"
    first_5_digits_of_Pi = "3.14159"
    print("ageMonths =",ageMonths)
    print("daysYear =",daysYear)
    print("firstPet =",firstPet)
    print("first_5_digits_of_Pi =",first_5_digits_of_Pi)
    

def expressions_practice():
    Literal = 10
    Addition = 5+19
    Exponent = 2**10
    Mod = 5%56
    multiplication = (59+2-19)*5
    mix_operators = 5+9-20*5/9
    print(Literal)
    print(Addition)
    print(Exponent)
    print(Mod)
    print(multiplication)
    print(mix_operators)
    


def prompt_and_print():
    inp=int(input("Enter a number: "))
    inp1=int(input("Enter another: "))
    print(inp,"+",inp1,"=",inp + inp1)
    print(inp,"-",inp1,"=",inp - inp1)
    print(inp,"*",inp1,"=",inp * inp1)
    print(inp,"/",inp1,"=",inp / inp1)


def Main():
    variables()
    expressions_practice()
    prompt_and_print()