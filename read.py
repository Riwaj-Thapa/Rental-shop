
def read_file():
    """ This method reads the file : path and returns 2D list of the same.
 """# Open the file named "items_name.txt"
    file = open("items_name.txt")
    # Read all lines from the file into a list
    data = file.readlines()
    # Close the file after reading
    file.close()
    # Initialize an empty list to store the 2D representation
    list2D = []
    for each in data:
        # Strip the line of leading and trailing spaces, then split it by commas
        list2D.append(each.strip().split(","))
    return list2D
    