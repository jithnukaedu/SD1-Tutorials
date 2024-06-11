n_1 = input("Please enter an integer: ")
n_2 = input("Please enter an integer which want to devide first entered integer: ")
try:
    n_1 = int(n_1)
    n_2 = int(n_2)
    print(n_1 / n_2)
except ZeroDivisionError:
    print("Cannot divide by zero")
