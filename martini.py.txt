import sys
'''
The Tech Test:
As for the test itself, we would like for you to create a martini glass in ASCII form. The height and width of this glass should be customizable based on input from a user. You don't need to have a GUI for this solution; a console input and output is just fine.

For my program I defined a method print_martini_glass(n) that takes in an integer to determine the width of the martini.
First it tests if n is a valid integer and that it is greater than 0.
'''
def draw_martini_glass(n):
    #First we test if n (users input value) is a valid integer for our script
    try:
        n = int(n)
    except ValueError:
        return "Error: Input must be an integer."
    #To ensure the input is a postive interger
    if n <= 0:
        return "Error: Input must be a positive integer."

   
   #We will initialize an empty list that will hold the contents of our martini glass.
    martini_glass = []

    #This is where we make the glass
    # We are using n as our width:
    width = n
    while width > 0:
        #This creates a row of the martini glass and adds it to the list based on the width value and centers the strings based on the value of n.
        martini_glass.append(('%' * width).center(n))
        # We look for the "special case" when the width is 2, meaning there should be one % under the width
        if width == 2:
            #This creates the row under for 2
            width -= 1
        else:
            #This allows us to create mulitple rows starting from 2
            width -= 2

    # Where we create the stem:
    
    # We need to determine if n is even or odd to see the placement of the stem
    if n % 2 == 0:  # If n is even we subtract one so it will be drawn on the left of the two columns
        stem_column = (n // 2) - 1
    else:  # If n is odd we draw it in the center
        stem_column = n // 2
    
    
    #N determine both the width and height of the glass, so we use in in this for each loop to add in both the empty spaces ' ' and the stem '|'    
    for i in range(n):
        row = [' '] * n
        row[stem_column] = '|'
        # Add it the list
        martini_glass.append(''.join(row))

    # To make the base of the glass we just have '=" be to the width and height of the glass, or n.
    martini_glass.append('=' * n)

    #We convert the list into a string and join each entry together with a line septorator inbetween which will create the glass shape.
    martini_string = '\n'.join(martini_glass)
    #We return the string
    return martini_string

if __name__ == "__main__":
    #If the program is run without arguements we can state instructions
    if len(sys.argv) != 2:
        print("Usage: python martini.py <width>")
        sys.exit(1)
    
    # We call on the function when an argument is provided, and the function determines if it is a valid input.
    result = draw_martini_glass(sys.argv[1])
    #Then we draw the glass
    print(result)