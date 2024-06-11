def negativePositiveZero(n):
    if n < 0:
        return 'negative'
    elif n > 0:
        return 'positive'
    else:
        return 'zero'
userValue = input('Enter a number: ')
userValue = float(userValue)
userResult = negativePositiveZero(userValue)
print(userValue, 'is', userResult)
