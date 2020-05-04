"""
CTEC 121
Sam Broyles
Module 3 Lab 1
Mod3/lab1 class demos
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

def main():
    """
    # conditional expressions

    # literal
    print("\nBoolean literals")
    print(True)
    print(False)
    print(type(True))
    print()

    #relational operators
    print("relational operators")
    print("3 < 5", 3 < 5)
    print("3 <== 3", 3 <= 3)
    print("3 == 3", 3 == 3)
    print("3 >= 5", 3 >= 5)
    print("3 != 5", 3 != 5)
    print()

    #using variables
    x = 3
    y = 5
    print("using variables")
    print("x:", x, "y:", y)
    print("x < y", x < y)
    print("x != y", x != y)
    print()

    #simple if statements
    print("x:", x, "y:", y)   
    if x < y:
        print("x < y")
    
    if x > y:
        print("x > y")

    print("end simple if example")
    print()

    # if/else statements
    print("if/else statement")
    print("x:", x, "y:", y)
    if x < y:
        print("x , y")
    else:
        print("x >= y")
    print()

    x = 6
    print("x:", x, "y:", y)
    if x < y:
        print("x , y")
    else:
        print("x >= y")
    print("end if/else example")
    print()

    #exercise 3-1
    for x in range(1, 11, 1):
        if  (x % 2) == 0:
            ans = "even"
        else:
            ans = "odd"    
        print(x, ans)
    print()

    # alphabetize names
    name = "Sam"
    firstLetterOfName = "S"

    print("Multiway if example")
    if firstLetterOfName == "A":
        print(name)
    elif firstLetterOfName == "B":
        print(name)
    elif firstLetterOfName == "C":
        print(name)
    #...
    elif firstLetterOfName == "Y":
        print(name)
    else:     # default case: name starts with "Z"
        print(name)
    print() 
    """
    try:
        print(4/0)
    except:
        print("\nThere was a divide by zero error. Exiting\n")
        exit()



main()    