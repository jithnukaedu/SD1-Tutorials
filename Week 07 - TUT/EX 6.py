def print_welcome_message():
    print("Welcome to Cavendish Pizzeria - choose your toppings.")
    print("When prompted, enter first letter or full word of operation.")

def print_menu():
    print("---- Operations ----")
    print("a: Add a topping")
    print("r: Remove a topping")
    print("c: Change a topping")
    print("o: Order the pizza")
    print("q: Quit")
    print("s: Start over")

def print_current_toppings(toppings):
    print("The toppings on your pizza are:", " ".join(toppings))

def main():
    toppings_list = []

    print_welcome_message()

    while True:
        print_menu()
        user_input = input("What would you like to do? add, remove, change, order, quit, startover: ").lower()

        if user_input == 'a':
            # Add a topping
            topping_to_add = input("Type in a topping to add: ")
            toppings_list.append(topping_to_add)
            print_current_toppings(toppings_list)

        elif user_input == 'r':
            # Remove a topping
            topping_to_remove = input("What topping would you like to remove: ")
            if topping_to_remove in toppings_list:
                toppings_list.remove(topping_to_remove)
                print_current_toppings(toppings_list)
            else:
                print(f"{topping_to_remove} is not on your pizza.")

        elif user_input == 'c':
            # Change a topping
            old_topping = input("Enter the topping to change: ")
            if old_topping in toppings_list:
                new_topping = input("Enter the new topping: ")
                index_to_change = toppings_list.index(old_topping)
                toppings_list[index_to_change] = new_topping
                print_current_toppings(toppings_list)
            else:
                print(f"{old_topping} is not on your pizza. Cannot change.")

        elif user_input == 'o':
            # Order the pizza
            print_current_toppings(toppings_list)
            print("Thanks for your order!")
            toppings_list = []  # Reset to an empty list

        elif user_input == 'q':
            # Quit
            print("Goodbye!")
            break

        elif user_input == 's':
            # Start over
            toppings_list = []
            print("Pizza toppings reset to start over.")

        else:
            print("I'm not sure what you said, please try again.")

if __name__ == "__main__":
    main()
