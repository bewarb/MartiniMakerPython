import sys

'''
The Tech Test:
As for the test itself, we would like for you to create a martini glass in ASCII form. The height and width of this glass should be customizable based on input from a user. You don't need to have a GUI for this solution; a console input and output is just fine.

For my program I defined a method print_martini_glass(n) that takes in an integer to determine the width of the martini.
'''

'''
Program Specifications:

The program should take a single integer argument, representing the width of the top of the glass, designated ‘n’. 

The bowl of glass should be composed of ‘%’ characters. It should be ‘n’ characters wide at the top, and 1 character wide at the bottom. Each row should be filled with ‘%’ characters

The bowl of the martini glass should narrow by 2 characters with every row, unless there are exactly 2 characters in the preceding row. In that case the next row should have 1 character. 

The martini glass should be left-biased. If an even number is submitted, the stem should  be drawn on column (n / 2)-1, e.g if n=4, it would draw on the 2nd column. 

The stem of the glass should be drawn of ‘|’ (pipe) characters, be 1 character wide, and ‘n’ characters in height. 

The base of the glass should be composed of ‘=’ characters, be ‘n’ characters wide, and 1 character tall. 

The program should error if given no argument, or an argument that is not a number.

The program should output nothing if given an invalid numeric argument
'''

def print_martini_glass(n):
    #
    if n == 2:
        print("%%")
        print("%")
    else:
        # Print the bowl of the glass
        for i in range(n, 0, -2):
            spaces = (n - i) // 2
            print(' ' * spaces + '%' * i)

    # Determine stem's position and print the stem
    # For n=2, this will correctly center the stem below the single '%'
    stem_position = (n // 2) - 1 if n > 2 else 0
    stem = ' ' * stem_position + '|'
    for _ in range(n):
        print(stem)
    
    #The base of the glass should be composed of ‘=’ characters, be ‘n’ characters wide, and 1 character tall. 
    print('=' * n)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        # The program should error if given no argument, or an argument that is not a number.
        print("Error: Please provide a integer argument for the width of the glass.")
        sys.exit(1)

    try:
        width = int(sys.argv[1])
        if width < 1:
            #The program should output nothing if given an invalid numeric argument
            print("The program expects a positive integer greater than 0.")
            sys.exit(1)
        print_martini_glass(width)
    except ValueError:
        print("Error: The argument provided is not a valid number.")
        sys.exit(1)

