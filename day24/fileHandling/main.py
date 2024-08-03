#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w 3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("day24/fileHandling/Input/Names/invited_names.txt") as f:
    names=f.readlines()
    for name in names:
        with open("day24/fileHandling/Input/Letters/starting_letter.txt") as f:
            letter=f.read()
            stripped_name=name.strip()
            new_letter=letter.replace("[name]",stripped_name)
            with open(f"day24/fileHandling/Output/ReadyToSend/{name}.txt",mode="w") as f:
                f.write(new_letter)
