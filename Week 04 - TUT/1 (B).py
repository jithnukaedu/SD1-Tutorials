import random

hidden = random.randint(1,20)
guess = int(input("Enter a number between 1 and 20: "))

while guess != hidden:
    print("The number was",hidden)
    print(guess,"is not correct")
    hidden = random.randint(1,20)
    guess = int(input("Enter a number between 1 and 20: "))
print(guess,"was correct")
