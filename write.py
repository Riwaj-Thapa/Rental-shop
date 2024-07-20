from os import system
from datetime import datetime as dt
from display import *

def write_bill_rent(name, contains):
    """
    The function creates a text file with the bill's name and current timestamp,
    writes the provided content to the file, and prints a confirmation message.
    """
    billName = ("Renting Bill "+name + str(dt.now())+".txt").replace(":", "-")
    file = open(billName, "w")
    file.write(contains)
    print(f"      {billName}")
    input("      (^_^)  THANKYOU FOR USING OUR SERVICE  (^_^)   ")
    system("cls")
    print(banner)
    
def write_bill_return(name, contains):
    """
    The function creates a text file with the bill's name and current timestamp,
    writes the provided content to the file, and prints a confirmation message.
    """
    billName = ("Returning Bill "+name + str(dt.now())+".txt").replace(":", "-")
    file = open(billName, "w")
    file.write(contains)
    print(f"      {billName}")
    input("      (^_^)  THANKYOU FOR USING OUR SERVICE  (^_^)   ")
    system("cls")
    print(banner)
    
def rent_bill(name, address, phone_number, days, raw_data, rented_items):
    """
    Generate a rental bill and return the bill's content as a string.
    
    Parameters:
    - name (str): Customer's name.
    - address (str): Customer's address.
    - phone_number (str): Customer's phone number.
    - days (int): Number of days the items were rented.
    - raw_data (list): List of raw item data, each item as a list [name, brand, rate].
    - rented_items (dict): Dictionary containing rented item indices as keys and quantities as values.
    
    """
    total_price = 0
    items_list = []

    for item_idx, qty in rented_items.items():
        item = raw_data [item_idx]
        item_name = item[0]
        item_brand = item[1]
        item_rate = float(item[2].replace("$", "").strip())
        days_to_work = days//5 + int (days % 5 > 0)
        cost_per_work_day= 5 * days_to_work
        item_total = (item_rate * qty * cost_per_work_day) 
        total_price += item_total
        items_list.append(f"|  {item_idx + 1:<5}|  {item_name:<31}|  {item_brand:<37}|  {qty:<9}|  {days_to_work:<12}|  ${item_rate:<8}|")                                        
    vat = round(0.13 * total_price, 2)
    grand_total = round(total_price + vat, 2)
     
    # f string is used to design the file format of the bill
    # we can write different strings and combine and write to file to create unique bill
    fileWrite = f"""
+========================================================================================================================+
|                                                   Easy Rentals                                                         |
|                                             Pokhara -17 ,Davi's fall                                                   |
|------------------------------------------------------------------------------------------------------------------------+
|   Name: {name:<30}                                                                                 |
|   Address: {address:<52}                                                        | 
|   Phone: {phone_number:<46}                                     Date: {dt.now().strftime('%Y-%m-%d')}           |                
|-------+---------------------------------+---------------------------------------+-----------+--------------+-----------+
|  S.N  |  Items                          |  Brand                                | Quantity  |  Work Days   |   Price   |
|-------+---------------------------------+---------------------------------------+-----------+--------------+-----------+
{chr(10).join(items_list)}
+-------+---------------------------------+---------------------------------------+-----------+--------------+-----------+      
|                                                                           Total:        ${total_price}                       
|                                                                           Vat: 13%      ${vat}                               
|                                                                           Grand Total:  ${grand_total}                       
+========================================================================================================================+             
"""
    print(fileWrite)
    write_bill_rent(name, fileWrite)

def return_bill(raw_data, returned_items,return_days, address, phone_number, name):
    """
    Generate a return bill for rented items, including fines for late returns.
    
    Parameters:
    - raw_data (list): List of raw item data, where each item is represented as a list [name, rate, brand].
    - returned_items (dict): Dictionary containing returned item indices as keys and quantities as values.
    - return_days (int): Number of days the items were returned late.
    - address (str): Customer's address.
    - phone_number (str): Customer's phone number.
    - name (str): Customer's name.
    
    """
    fine_per_day = 10  
    rental_days = 5  

    return_date = dt. now()

    vat_rate = 0.13  # 13%
    total_price = 0
    fine_total = 0
    item_lines = []

    for item_idx in returned_items.keys():
        if item_idx - 1 < len(raw_data):
            item = raw_data[item_idx - 1]
            item_name, item_rate, item_brand= item[0], float(item[2].replace("$", "").strip()), item[1]
            late_days = max(0, return_days - rental_days)
            fine = late_days * fine_per_day
            fine_total += fine

            item_total = item_rate * returned_items[item_idx]
            total_price += item_total

            item_lines.append(f"|  {item_name:<38}|  {item_brand:<37}| ${fine:<6}  |")

    vat = round(vat_rate * total_price, 2)
    grand_total = total_price + fine_total + vat

    invoice_text = f"""
+===========================================================================================+
|                                        Easy Rentals                                       |                 
|                                 Pokhara -17 ,Davi's fall                                  |                
|-------------------------------------------------------------------------------------------+
|  Name: {name:<25}                                                          |
|  Address: {address:<25}                                                       |
|  Phone: {phone_number}                        Return Date: {return_date.strftime('%Y-%m-%d')}                         |
+----------------------------------------+---------------------------------------+----------+
|         Items                          |  Brand                                |  Fine    |  
+----------------------------------------+---------------------------------------+----------+
{chr(10).join(item_lines)}
+----------------------------------------+---------------------------------------+----------+
|                                                       Total:       ${total_price:.2f}             
|                                                       Fine:        ${fine_total:.2f}              
|                                                       Vat: 13%     ${vat:.2f}             
|                                                       Grand Total: ${grand_total:.2f}            
+===========================================================================================+
"""
    print(invoice_text)
    write_bill_return(name, invoice_text)

