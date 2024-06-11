while True:
    try:
        option = int(input("Select option 1,2,3 or 4 to quit: "))

        if option == 1 or option == 2 or option == 3:
            print(option,"selected")

        elif option == 4:
            print("Quit selected")
            break

        else:
            print("Option not recognized")

    except ValueError:
        print("Enter integer")
            
        
