import random
import string

def generate_password(length):
    if length < 6:
        raise ValueError(f"Your password is too short. Pick a password above 6 characters. You only picked {length}.")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(numbers),
        random.choice(symbols)
    ]

    complete_password = lowercase + uppercase + numbers + symbols
    password += random.choices(complete_password, k=length - 4)  
    random.shuffle(password)
    return ''.join(password)

print("Welcome to password generator!")

while True:
    try:
        password_length = int(input("How long do you want your password to be? "))
        password = generate_password(password_length)
        print(f"Generated Password: {password}")
        break  
    except ValueError as e:
        print(e)  