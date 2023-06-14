alphabet = 'abcdefghijklmnopqrstuvwxyz '

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def transform_text(text, shift_amount):
    transformed_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % len(alphabet)
            transformed_text += alphabet[new_position]
        else:
            transformed_text += letter
    return transformed_text

def encrypt(plain_text, shift_amount):
    cipher_text = transform_text(plain_text, shift_amount)
    print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_amount):
    plain_text = transform_text(cipher_text, -shift_amount)
    print(f"The decoded text is {plain_text}")

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
