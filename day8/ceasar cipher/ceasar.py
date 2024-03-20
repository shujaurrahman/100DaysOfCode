alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar(start_text,shift_amount,cipher_direction):
    end_text=""
    for letter in start_text:
        position=alphabet.index(letter)
        if cipher_direction=="decode":
            shift_amount*=-1
        new_position=position+shift_amount
        new_letter=alphabet[new_position]
        end_text+=new_letter
    print(f"The {direction}d text is {end_text}")
cipher=True
while(cipher):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%26 
    ceasar(start_text=text,shift_amount=shift,cipher_direction=direction)
    print("Type 'Yes' if you want to go again. Otherwise type no ")
    state=input().lower()
    if(state=="no"):
        cipher=False
    elif state=="yes":
        cipher=True
    else:
        print("Type valid input.")
    if(not cipher):
        break
print("Thankyou, For your time.")
