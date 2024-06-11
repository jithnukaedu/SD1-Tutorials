secret = "python"
turns = len(secret)
guesses = " "
count = 0
print("let's play Guess the word\nYou have 6 turns to guess the word!")
print("_ "*5)
while turns>0:
    guess = input("\nEnter a letter: ")
    if len(guess) == 1:
        guesses = guesses + guess
        guesses = guesses.lower()
        for letter in secret:
            if letter in guesses:
                print('', letter, '', end='')
            else:
                print(' _ ', end='')
    else:
        guesses = guesses + guess[0]
        guesses = guesses.lower()
        for letter in secret:
            if letter in guesses:
                print('', letter, '', end='')
            else:
                print(' _ ', end='')  
    turns= turns-1   
print("\nEnd of Game")
