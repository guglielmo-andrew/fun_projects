#A simple calulator that continues to tally a total.

#Functions
def float_to_int(i):
    '''A funcation to remove the '.0' from the end of a number. The fucntion returns the intger form
    of the number or the original number passed in.'''
    if i % int(i) == 0: #Getting rid of '.0' 
        i = int(i)
    return i

def calc(number1, operator, number2):
    '''A function to add, subtract, multiply, and divide two numbers and retun the total.
    Numbers are integers and the operator is a string. All three are user input.'''
    if operator == "+":
        total = number1 + number2   

    elif b == "-":
        total = number1 - number2
        
    elif b == "*":
        total = number1 * number2

    elif b == "/":
        total = number1 / number2
    
    return total

# Main portion of the program
operators = ["+", "-", "*", "/"]
print("Calulator - Enter your numbers. Use CTRL-C and then Enter to quit.")
a = int(input("Number: "))

try:
    b = ""
    while b not in operators:
        b = input("Operator: ")
        if b not in operators: 
            print("Must be an operator like +, -, *, /")

    c = int(input("Number: "))

    #Pass values to caluator funciton and store as total
    total = calc(a, b, c)

    total = float_to_int(total)
    print("Total: {}".format(total))
    
    while True:
        b = ""
        while b not in operators:
            b = input("Operator: ")
            if b not in operators: 
                print("Must be an operator like +, -, *, /")

        c = int(input("Number: "))

        total = calc(total, b, c)

        total = float_to_int(total)
        print("Total: {}".format(total))

except KeyboardInterrupt:
    print("Exiting.")