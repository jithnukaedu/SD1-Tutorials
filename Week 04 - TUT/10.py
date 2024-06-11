import random

hidden = random.randint(1,20)
guessesTaken = 0

while guessesTaken < 5:
    guess = int(input("Enter a guess (number between 1 and 20): "))
    guessesTaken = guessesTaken + 1

    if guess == hidden:
        print("You got it in",guessesTaken,"guesses")
        break

    elif guess < hidden:
        print("Your guess is too low")

    else:
        print("Your guess is too high")

else:
    print("Not guessed. The correct answer was: ",hidden)
        
    
