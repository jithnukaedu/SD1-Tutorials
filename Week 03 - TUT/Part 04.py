#and (b)
m = int(input('Give me number between 1 and 10:'))
if m>=1 and m<11:
    print('Well done! You gave me: ',m)

#or (d)
mark = int(input("Enter your mark: "))
if mark<=0 or mark>100:
    print("Mark is invalid")
elif mark >= 70:
    print('Exceptional result!')
elif mark >= 40:
    print('Satisfactory result!')
else:
    print("You have failed.")

#not (f)
x = 10
if not x > 10:
    print("not returned True")
else:
    print("not returned False")
