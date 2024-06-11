secret = "python"
turns = len(secret)
guesses = " "
missed = len(secret)

print("Let's play Guess the word\nYou have 6 turns to guess the word!")
print("_ " * len(secret))

while turns > 0 and missed > 0:
    guess = input("\nEnter a letter or a word: ").lower()

    if len(guess) > 1 and guess.isalpha():
        # Take the first letter of the word
        guess = guess[0]

    if len(guess) == 1 and guess.isalpha():
        guesses += guess
        if guess not in secret:
            turns -= 1
            print("Wrong guess! Turns left:", turns)
        else:
            print("Good guess!")

        missed = 0  # Reset missed count for this iteration
        for letter in secret:
            if letter in guesses:
                print('', letter, '', end='')
            else:
                print(' _ ', end='')
                missed += 1
    else:
        print("Please enter a valid single letter or word.")

if missed == 0:
    print("\nCongratulations! You guessed the word!")
else:
    print(f"\nSorry, you ran out of turns. The word was '{secret}'.")
