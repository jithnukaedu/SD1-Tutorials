def negativePositiveZero(n):
    if n < 0:
        return 'negative'
    elif n > 0:
        return 'positive'
    else:
        return 'zero'

result = negativePositiveZero(-25.7)
print('-25.7 is', result)

result = negativePositiveZero(0.0)
print('0.0 is', result)

result = negativePositiveZero(123.45)
print('123.45 is', result)
