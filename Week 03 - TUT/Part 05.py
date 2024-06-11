user_input = input("Do you like Python? (yes/no):\n")
user_input = user_input.lower()
if user_input == "yes":
    print("you are on the right course")
elif user_input == "no":
    print("you might change your mind")
else:
    print("I did not understand")
