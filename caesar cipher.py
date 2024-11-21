def caesar_cipher(message, shift, mode):
    result = ""
    if mode == 'decrypt':
        shift = -shift

    for char in message:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) + shift - shift_amount) % 26 + shift_amount)
        else:
            result += char

    return result

if __name__ == "__main__":
    mode = input("Do you want to encrypt or decrypt the message? (enter 'encrypt' or 'decrypt'): ").strip().lower()
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    if mode in ['encrypt', 'decrypt']:
        result = caesar_cipher(message, shift, mode)
        print(f"The {mode}ed message is: {result}")
    else:
        print("Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")
