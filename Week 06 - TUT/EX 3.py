# Loops - Seminar
# Exercise 3 - Revision of exception handling.

while True:
    n = input("Please enter an integer: ")
    try:
        n = int(n)
        break                      # break or continue
    except ValueError:
        print("Requires a valid integer! Please try again.")

print("You successfully entered an integer.")
