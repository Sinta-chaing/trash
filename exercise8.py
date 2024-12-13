
# loop
#the ASCII values of uppercase English alphabet letters
for i in range(65, 91): 
    #escape B J O U X Z
    if chr(i) == "B" or chr(i) == "J" or chr(i) == "O" or chr(i) == "U" or  chr(i) == "X"or chr(i) == "Z":
        pass # it skip the alphabet
    
    else:
        # find the alphabet in the string
        count = "GIVEQCCTSICSLYQLENYCNFVNQHLCGSHLVEALYLVCGERGFFYTPKTNQHERGFFYTPKSICSLYQLVCGEVEQCCTTSICSLYLCGSHRGFFYTLVECGEALYLHERGICSLYQLENYCNFVNQHLCGSHLVEALYLVCGERGFFYTPKTNQHERGFFYTPKSICSLYQLVCGEVEQCCTTSICSLYLCGSQCCTTSICSLYLCGSHRGFFYTLVECGEALYLHERGICSLYQLENYCNFVNQHL".count(chr(i))
        
        #show the result
        print(chr(i),"=",count)
