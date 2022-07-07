alphabet = ['a', 'b', 'c']
plain_text = input("whats the massage\n")
shift = 1

cipher = ""    
for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift
    if new_position >= len(alphabet):
        new_position = position - shift
    encoded = alphabet[new_position]
    cipher += encoded 
print(f"your encoded text is {cipher}")

