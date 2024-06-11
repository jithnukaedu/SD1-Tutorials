mark = input("Please enter your mark: ")
mark = int(mark)
if mark<40:
    print('Fail')
else:
    print("Pass")

#Little bit advaced code

def check_pass_fail(mark):
    if mark<40:
        print('Fail')
    elif mark>100:
        print("Entered mark is not valid")
    else:
        print("Pass")

for mark in range(0,100):
    mark = input("Please enter your mark: ")
    mark = int(mark)
    check_pass_fail(mark)
