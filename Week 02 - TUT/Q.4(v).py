print("convert the string input to an integer")
num_1 = input('Enter number one: ')
num_2 = input('Enter number two: ')
num_1 = int(num_1)
num_2 = int(num_2)
total = num_1 + num_2
print(total)

print("convert the string input to a float.")
cost = float(input('Enter cost of item: '))
paid = float(input('Enter cash paid: '))
change = paid - cost
print('Change is: ', float(change))

print("calculate the average of three numbers")
num_1 = int(input('Enter number one: '))
num_2 = int(input('Enter number two: '))
num_3 = int(input('Enter number three: '))
average = (num_1+num_2+num_3)/3
print("Average of three numbers: ", round(average,3))
