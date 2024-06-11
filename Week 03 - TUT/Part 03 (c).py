cost = float(input("Enter the cost of the meal: "))
rating = input("""Indicate satisfaction level
1 = Totally satisfied
2 = Satisfied
3 = Dissatisfied
: """)

if rating == '1':
    tip = cost * 0.2
elif rating == '2':
    tip = cost * 0.15
else:
    tip = cost * 0.1

print(tip)
