alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))




def caesar(start_text,shift_amount,cipher_direction):

    end_text = ""
    if  cipher_direction == "decode":
        shift_amount = shift_amount * -1
    for letters in start_text:
        position = alphabet.index(letters)
        new_position = position + shift_amount
        encoded = alphabet[new_position]
        end_text += encoded
    print(f"your {direction}d text is {end_text}")


caesar(text,shift,direction)
 
     
   


  







#version 1

# def caesar(text,shift,direction):

#     cipher = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         if new_position >= len(alphabet):
#             new_position = position - shift
#         encoded = alphabet[new_position]
#         cipher += encoded
#     print(f"your encoded text is {cipher}")

#     cipher = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position - shift
#         encoded = alphabet[new_position]
#         cipher += encoded
#     print(f"your decoded text is {cipher}")










