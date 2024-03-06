import sys
'''
The Tech Test:
As for the test itself, we would like for you to create a martini glass in ASCII form. The height and width of this glass should be customizable based on input from a user. You don't need to have a GUI for this solution; a console input and output is just fine.

For my program I defined a method print_martini_glass(n) that takes in an integer to determine the width of the martini.
First it tests if n is a valid integer and that it is greater than 0.
'''
def draw_martini_glass(n):
    try:
        n = int(n)
    except ValueError:
        return "Error: Input must be an integer."
    
    if n <= 0:
        return "Error: Input must be a positive integer."

   
   #We will initial
    martini_glass = []

    # If n
    width = n
    while width > 0:
        martini_glass.append(('%' * width).center(n))
        if width == 2:
            width -= 1
        else:
            width -= 2

    # Draw the stem
    stem_column = (n // 2) - 1 if n % 2 == 0 else n // 2
    for _ in range(n):
        row = [' '] * n
        row[stem_column] = '|'
        martini_glass.append(''.join(row))

    # Draw the base
    martini_glass.append('=' * n)

    return '\n'.join(martini_glass)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python martini.py <width>")
        sys.exit(1)
    
    result = draw_martini_glass(sys.argv[1])
    print(result)