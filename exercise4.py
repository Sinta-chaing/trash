#Exercise 04

total = 0

for i in range(1, 31):
    if i % 2 == 1:  # Odd numbers are added
        total += i
    else:  # Even numbers are subtracted
        total -= i

print("The total is: ",total)
