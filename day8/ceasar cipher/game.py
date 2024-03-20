alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrpt(plain_text,shift_amount):
    cipher_text=""
    for letter in plain_text:
        position=alphabet.index(letter)
        new_position=position+shift_amount
        new_letter=alphabet[new_position]
        cipher_text+=new_letter
    return cipher_text


def decrypt(plain_text,shift_amount):
    dichiper_text=""
    for letter in plain_text:
        position=alphabet.index(letter)
        real_position=position-shift_amount
        real_letter=alphabet[real_position]
        dichiper_text+=real_letter
    return dichiper_text

ciphering=True
while(True):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction=="encode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encyted_data=encrpt(plain_text=text,shift_amount=shift)
        print(f"The encoded text is {encyted_data} ")

    if direction=="decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypted_data=decrypt(plain_text=text,shift_amount=shift)
        print(f"The decoded text is {decrypted_data} ")

    print("Continue Ciphering, Type 'Yes' or 'No': ")
    game_state=input().lower()
    if game_state=="yes":
        ciphering=True
    else:
        ciphering=False
    if(not ciphering):
        break