count = 0  # Counter to keep track of numbers per line

for i in range(100, 201):
    # Check if the number is divisible by both 5 and 6
    if i % 5 == 0 and i % 6 == 0:
        continue # Skip this number if it is divisible by both 5 and 6
    
    # Check if the number is divisible by 5 or 6, but not both
    if i % 5 == 0 or i % 6 == 0:
        print(i, end="\t")
        count += 1
        
        # Print a newline after every 10 numbers
        if count == 10:
            print()
            count = 0  # Reset count for the next line
