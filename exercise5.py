computer_num = 50
count = 0 # Initialize attempt counter

while True:
    # Ask the user for a number input
    number = eval(input("Enter a number: "))
    count += 1 # Increment attempt counter
    
    if number < computer_num:
        print("Too low")
    elif number > computer_num:
        print("Too high")
    else:
        print("Well done, you took", count, "attempts.")
        break # Exit the loop when the correct number is guessed