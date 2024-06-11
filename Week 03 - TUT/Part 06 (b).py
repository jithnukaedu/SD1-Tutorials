try:
    age = int(input("Enter your age: "))
    if age >= 18:
        print("Can vote")
except ValueError:
    print("Please enter an integer")
