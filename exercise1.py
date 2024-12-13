#Exercise 01
#Prompt for user input
M_in_kg = eval(input("Please enter the amount of water: "))
initial_temp = eval(input("Enter the initial temperatures: "))
final_temp = eval(input("Enter the final temperatures: "))

# Calculate the energy Q using the formula Q = m * c * ΔT
# where m is mass in kg, c is the specific heat capacity (4184 J/(kg°C)), and ΔT is the temperature difference
Q = M_in_kg * (final_temp - initial_temp) * 4184

print("The energy Q is: ", Q, "jouls")
