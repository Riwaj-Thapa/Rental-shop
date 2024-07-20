# Importing necessary modules
from display import *
from os import system
import operations

# Clear the screen
system("cls")
# Print the banner
print(banner)
# Initialize the main loop
i = True
while (i):
    # Start try catch block
    try:
        # Print the available options
        print(options)
        # Get the user's choice
        choice_num = int(input("      Enter the number to choose :----->"))
        # Check the user's choice and perform corresponding actions
        if choice_num == 1:
            display_table()  # Display the table of items
        elif choice_num == 2:
            operations.rent_items()  # Call function to rent items
        elif choice_num == 3:
            operations.return_items()  # Call function to return items
        elif choice_num == 69:
            system("cls")  # Clear the screen
            print(banner)  # Print the banner
            print("\n      (^_^)  THANKYOU FOR VISITING US  (^_^)")
            break  # Exit the loop
        else:
            print("\n      Choose the correct Options")
    except:
        # Handle exceptions gracefully
        system("cls")  # Clear the screen
        print(banner)  # Print the banner
        print("\n        ###  Please choose the correct options  ###")
    # End of the main loop
