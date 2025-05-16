import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True):
    # Define character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    # Create the character pool
    char_pool = ''
    if use_uppercase:
        char_pool += uppercase_letters
    if use_lowercase:
        char_pool += lowercase_letters
    if use_digits:
        char_pool += digits
    if use_symbols:
        char_pool += symbols

    if not char_pool:
        raise ValueError("At least one character type must be selected!")

    # Generate password by randomly choosing from the pool
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

# Ask user for preferences
if __name__ == "__main__":
    print("Welcome to the Password Generator!")

    try:
        length = int(input("Enter password length (e.g., 12): "))
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
        print(f"\nGenerated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")
