#Exercise 02

# Prompt the user to select an option for area calculation
choice = input("Select an option:\n1. Area of a square\n2. Area of a triangle\n")

# if elif else.. statement
if choice == '1':
    side = eval(input("Enter the length of one side of square: "))
    area = side * side
    print("The area of the square is:", area, "m2")
elif choice == '2':  
    base = eval(input("Enter the base of triangle: "))
    height = eval(input("Enter the height of triangle"))
    area = 0.5 * base * height
    print("The area of the triangle is:", area, "m2")
else:
    print("Invalid choice! Please enter 1 or 2.")
