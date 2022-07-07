alphabet = ['a']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Encryption Function

def encrypt(plain_text,shift_amount):

    cipher = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        if new_position >= len(alphabet):
            new_position = position - shift
        encoded = alphabet[new_position]
        cipher += encoded
    print(f"your encoded text is {cipher}")
            






# Decryption Function

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt (text,shift):


  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"
    cipher = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position - shift
        encoded = alphabet[new_position]
        cipher += encoded
    print(f"your decoded text is {cipher}")



#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if input == "encode":
    encrypt(text , shift)
elif input == "decode":
    decrypt(text , shift)