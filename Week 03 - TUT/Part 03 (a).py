user_input = input("Enter '1' to convert from Celsius to Fahrenheit \nEnter '2' to convert from Fahrenheit to Celsius : ")

if user_input == '1':
    c = float(input("Enter a temperature in the correct unit: "))
    f = (c * 1.8) + 32
    print(c,"Centigrades =",f,"Fahrenheits")
elif user_input == '2':
    f = float(input("Enter a temperature in the correct unit: "))
    c = (f - 32) / 1.8
    print(f,"Fahrenheits =",c,"Centigrades")

else:
    print("Invalid option entered")

