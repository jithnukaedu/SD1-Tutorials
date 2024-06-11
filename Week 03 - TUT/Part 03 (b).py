# Initializing variables
num1 = 0
num2 = 0
ope = ""

# Getting the user input
num1 = int(input("Enter first value:"))
ope = input("Enter operator (+,-,*,/):")
num2 = int(input("Enter second value:"))

# Performing the calculation
if(ope == '+'):
    answer = num1 + num2
elif(ope == '-'):
    answer = num1 - num2
elif(op == '*'):
    answer = num1 * num2
elif(ope == '/'):
    answer = num1 / num2
else:
    print("Invalid inputs")

print(answer)
