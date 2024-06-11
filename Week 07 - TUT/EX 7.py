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

def print_pizza_toppings(toppings):
    if not toppings:
        print("No toppings on your pizza.")
    else:
        print("The toppings on your pizza are:", " ".join(toppings))

def add_topping(toppings_list):
    topping_to_add = input("Type in a topping to add: ")
    toppings_list.append(topping_to_add)
    print_pizza_toppings(toppings_list)

def remove_topping(toppings_list):
    topping_to_remove = input("What topping would you like to remove: ")
    if topping_to_remove in toppings_list:
        toppings_list.remove(topping_to_remove)
        print_pizza_toppings(toppings_list)
    else:
        print(f"{topping_to_remove} is not on your pizza.")

def change_topping(toppings_list):
    old_topping = input("Enter the topping to change: ")
    if old_topping in toppings_list:
        new_topping = input("Enter the new topping: ")
        index_to_change = toppings_list.index(old_topping)
        toppings_list[index_to_change] = new_topping
        print_pizza_toppings(toppings_list)
    else:
        print(f"{old_topping} is not on your pizza. Cannot change.")

def order_pizza(toppings_list):
    print_pizza_toppings(toppings_list)
    print("Thanks for your order!")
    toppings_list.clear()  # Reset to an empty list

def start_over(toppings_list):
    toppings_list.clear()
    print("Pizza toppings reset to start over.")

def main():
    toppings_list = []

    print_welcome_message()

    while True:
        print_menu()
        user_input = input("What would you like to do? add, remove, change, order, quit, startover: ").lower()

        if user_input == 'a':
            add_topping(toppings_list)

        elif user_input == 'r':
            remove_topping(toppings_list)

        elif user_input == 'c':
            change_topping(toppings_list)

        elif user_input == 'o':
            order_pizza(toppings_list)

        elif user_input == 'q':
            print("Goodbye!")
            break

        elif user_input == 's':
            start_over(toppings_list)

        else:
            print("I'm not sure what you said, please try again.")

if __name__ == "__main__":
    main()
