hidden = 6
guess = int(input("Enter a number between 1 and 20: "))
while guess != hidden:
    print(guess,"is not correct")
    guess = int(input("Enter a number between 1 and 20: "))
print(guess,"was correct")
