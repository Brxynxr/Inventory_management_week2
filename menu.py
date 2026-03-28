from add_product import add_product
from show_inventory import show_inventory
from statistics import calculate_statistics
 
def menu():
    running = True
    # The loop keeps the program active until the user chooses to exit
    while running:
 
        # We display the available options
        print("\n---------- MAIN MENU ----------")
        print("1. Add product")
        print("2. Show inventory")
        print("3. Calculate statistics")
        print("4. Exit")
        option = input("→ Select an option: ")
        print("------------------------------------")
 
        # We use conditionals to run the action based on the chosen option
        if option == "1":
            add_product()
        elif option == "2":
            show_inventory()
        elif option == "3":
            calculate_statistics()
        elif option == "4":
            print("Exiting the system...")
            running = False
        else:
            # If the option is not valid, the program does not close, it just shows a warning
            print("Invalid option. Please try again.")
