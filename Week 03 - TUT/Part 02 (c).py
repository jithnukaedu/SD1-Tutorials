try:
    num = input("Enter a number: ")
    num = int(num)
    if num % 2 == 0 :
        print(f"{num} is an even")
    else:
        print(f"{num} is an odd")
except:
    print(f"{num} is invalid")
