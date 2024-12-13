#let user input the color
user = input("enter your favorite color: ")
color = "red"

# if the user input color red RED Red then display
if user == color.lower() or user == color.upper() or user == color.capitalize():
    print("i like red too")
    #emoji
    print(chr(128512), "\U0001F970")
    
    #else display dont like
else:
    print("i don't like", user, ", i prefer red")
    print("\U0001F62D")
