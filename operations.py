from os import system
from display import *  
import read  
import write

def decrease_quantity(items, quantity):
    """
    This function reads information about items from a file,
    verifies whether the specified item exists, and validates
    if there's enough stock to decrease by the specified quantity.
    If both of these conditions are satisfied, it proceeds to update
    the stock in the data file and then returns True to indicate a 
    successful update.
    """
    try:
        file_decrease = open("items_name.txt")
        data_decrease = file_decrease.readlines()
        
        if items > 0 and items <= len(data_decrease):
            item_data = data_decrease[items - 1].strip().split(',')
            current_quantity = int(item_data[3])
            
            if current_quantity >= quantity:
                new_quantity = current_quantity - quantity
                item_data[3] = str(new_quantity)
                data_decrease[items - 1] = ','.join(item_data) + '\n'
                
                file_decrease= open("items_name.txt", mode="w")
                file_decrease.writelines(data_decrease)
                file_decrease.close()
                
                return True
            else:
                print("      !! Item out of stock !!")
                return False
        else:
            print("      !!  Please enter the item from the table  !!")
            return False
    except: 
        print("      !! Error Found  !!")
        return False

def rent_items():
    """
    Display a table of available items, allow the user to rent items, and generate a rental bill.

    This function displays a table of available items, allows the user to select and rent items, and
    generates a rental bill based on the selected items, quantity, rental duration, and customer information.

    The user is prompted to enter their name, address, phone number, and the number of days they want
    to rent the items. The function validates user inputs and ensures that the selected items are in stock.

    The rental bill is generated using the 'write.rent_bill' function.

    """
    system("cls")
    display_table()
    rented_items = {}
    i=True
    while(i):
        try:
            raw_data = read.read_file()
            selected_items = int(input("\n      Enter the correct SN to rent items ----> "))
            
            # checking whether the selected items variable is more than one and less than the items list found.
            if selected_items < 1 or selected_items > len(raw_data):
                print("       !! The item selected is not in the list !!")
                continue
            
            # checking  whether the quantity variable is zero or more than the quantity available in table.
            while(True):
                try:
                    quantity = int(input("\n      Enter the number of quantity you need ----> "))
                    if quantity <= 0 or quantity > int(raw_data[selected_items - 1][3]):
                        print("       !! The selected quantity is out of stock !!")
                    else:
                        break
                except:
                    print("      !! Enter the correct value for quantity !!")
            
            if decrease_quantity(selected_items, quantity):
                quantity_before = int(raw_data[selected_items - 1][3])
                quantity_after = quantity_before - quantity
                raw_data[selected_items - 1][3] = str(quantity_after)
                rented_items[selected_items - 1] = quantity
                
                system("cls")
                display_table()
                
                user_choice = input("\n      +++++ Press A/a to rent other items or any other key to continue +++++ ").lower()
                if user_choice != 'a':
                    i = False
            
        except:
            system("cls")
            display_table()
            print("      !! Please choose correct SN number to rent items !!")
        
    if rented_items:
            print("\n      ! Calculation is done on basis for 5 days !\n ")
            
    # checking  whether the days variable takes only positive value.
    while(True):
        try:
            days = int(input("      Enter the days you want to rent the items:----> "))
            if days <= 0:
                print("      Items cannot be rented below 1 day")
            else:
                break
        except:
            print("       Please enter the days in numerical value")
        
    # checking  whether the name variable takes only alphabetical value or not.        
    while(True):
        name = input("\n      Please enter your name : ")
        if any(char.isdigit() for char in name):
            print("      Name only cotains alphabetical values")
                        
        elif any(char.isspace() for char in name):
                print("      !! Please enter only alphabetical values without spaces !!")
        else:
            break
        
    # Checking wether the address is alpha-numeric or not.   
    while (True):
        address = input("\n      Please enter your address : ")
                    
        if any(char.isalpha() for char in address) or any(char.isdigit() for char in address):
            break
        else:
            print("      !!!  Address must contain alpha_numeric value  !!! ")
        
    # Checking if phone number digits is less or more than 10 digits
    while (True):
          
        phone_number = input("\n      Please enter your phone number :")
                    
        if phone_number.isdigit() and len(phone_number) == 10:        
            break
        else:
            print("      !! Please enter your phone number in 10 digits !!")
        
    write.rent_bill(name, address, phone_number, days, raw_data, rented_items)
    

def increase_quantity(items, quantity):
    """
    This function reads information about items from a file,
    verifies whether the specified item exists, and validates
    increase by the specified quantity.If both of these conditions
    are satisfied, it proceeds to update the stock in the data 
    file and then returns True to indicate a successful update.
    """
    try:
        file_increase = open("items_name.txt")
        data_increase = file_increase.readlines()

        if items > 0 and items <= len(data_increase):
            item_data = data_increase[items - 1].strip().split(',')
            
            if len(item_data) >= 4:  # Ensure the item_data has at least 4 values
                current_quantity = int(item_data[3])
                new_quantity = current_quantity + quantity
                item_data[3] = str(new_quantity)
                data_increase[items - 1] = ','.join(item_data) + '\n'

                file_increase = open("items_name.txt", mode="w")
                file_increase.writelines(data_increase)
                file_increase.close()

                return True
            else:
                print("      !! Item out of stock !!")
                return False
        else:
            print("      !!  Please enter the item from the table  !!")
            return False
    except:
        print("      !! Error Found  !!")
        return False
    

def return_items():
    """
    Display a table of rented items, allow the user to return items, calculate fines, and generate a return bill.

    This function displays a table of rented items, allows the user to select and return items, calculates fines for late returns,
    and generates a return bill based on the returned items, rental duration, and customer information.

    The user is prompted to enter their name, address, phone number, the number of days after returning the items, and the quantity
    of items they want to return. The function validates user inputs and ensures that the selected items are rented.

    The return bill is generated using the 'write.return_bill' function.
    
    """
    system("cls") 
    display_table()
    returned_items = {}
    i = True
   
    while(i):
        try:
            raw_data = read.read_file()
            selected_items = int(input("\n      Enter the correct SN to return items ----> "))
           
            # Checking wether the selected_items variable is in table ore not.
            if selected_items < 1 or selected_items > len(raw_data):
                print("       !! The item selected is not in the list !!")
                continue
            
            # Checking wether the quantity_return variable is more than zero or not.
            while(True):
                try:
                    quantity_return = int(input("\n      Enter the quantity of items you want to return ---->"))
                    if quantity_return <= 0:
                        print("      !! The minimum quantity to return rented item is one !! ")
                    else:
                        break
                except:
                    print("      Please enter the days in numerical value")  
           
             
            if increase_quantity(selected_items, quantity_return):
                before = int(raw_data[selected_items - 1][3])
                after = before + quantity_return  # Increment by the returned quantity
                raw_data[selected_items - 1][3] = str(after)
                returned_items[selected_items] = quantity_return  # Store returned items in the dictionary

                system("cls")
                display_table()           
                user_choice = input("\n      +++++ Press A/a to return other items or any other key to continue +++++ ").lower()
                if user_choice != 'a':
                    i = False
        except:
            system("cls")
            display_table()
            print("      !! Please choose correct SN number to rent items !!")
            
           
    if returned_items:
        # Checking wether the return_days variable is more than one or not.
        while(True):
                try:
                    print("\n\n      ###  Fine will be charged per day $10 /- returning after 5 days  ###")
                    return_days = int(input("\n      Enter the days after you returned the item---->"))
                    if return_days < 1:
                        print("      !! The items rented cannot be returned within the days !! ")
                    else:
                        break
                except:
                    print("      Please enter the days in numerical value")
                     
        # Checking whether the name variable contains space or number or not.
        while(True):
            name = input("\n      Please enter your name : ")
            if any(char.isdigit() for char in name):
                print("      Name only cotains alphabetical values")
                            
            elif any(char.isspace() for char in name):
                    print("      !! Please enter only alphabetical values without spaces !!")
            else:
                break
        
        
        # Checking whether the address is alpha-numeric or not.   
        while (True):
            address = input("\n      Please enter your address : ")
                        
            if any(char.isalpha() for char in address) or any(char.isdigit() for char in address):
                break
            else:
                print("      !!!  Address must contain alpha_numeric value  !!! ")
            
        # Checking if phone number digits is less or more than 10 digits
        while (True):
            
            phone_number = input("\n      Please enter your phone number :")
                        
            if phone_number.isdigit() and len(phone_number) == 10:        
                break
            else:
                print("      !! Please enter your phone number in 10 digits !!")
            

        write.return_bill(raw_data, returned_items,return_days,address, phone_number, name)

    
