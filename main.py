alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(text, shift_amount, direction):
    result_text = ""
    if direction == "decrypt":
        shift_amount = -shift_amount

    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % len(alphabet)
            result_text += alphabet[new_position]
        else:
            result_text += letter
    return result_text

direction = input("Type 'encrypt' to encrypt, type 'decrypt' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction in ['encrypt', 'decrypt']:
    processed_text = caesar_cipher(text, shift, direction)
    print(f"Your {direction}ed text is: {processed_text}")
else:
    print("Invalid command.")
