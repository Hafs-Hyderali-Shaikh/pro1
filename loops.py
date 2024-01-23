def countdown(number):
    sum = 0
    while number >= 0:
        print(number)
        sum += number
        number -= 1
    return sum



def count_up(numb):
    sum = 0
    while numb >= 0:
        print(numb)
        sum += numb
        numb -= 1
    return sum

def main():
    number = int(input("Enter a number for the countdown: "))
    sum_result = countdown(number)
    print("Sum of the countdown numbers:", sum_result)
    numb= int(input("Enter a number for the countup: "))
    sum_result1 = count_up(numb)
    print("Sum of the countup numbers:", sum_result1)
    
main()
    
    