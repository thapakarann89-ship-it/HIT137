def encrypt(text, shift1, shift2):
    result = []
    for char in text:
        if char.islower():
            if 'a' <= char <= 'm':
                beginning = ord('a')
                shift = (shift1 * shift2) % 13
                result.append(chr(beginning + ((ord(char) - beginning + shift) % 13)))
            elif 'n' <= char <= 'z':
                beginning = ord('n')
                shift = (shift1 + shift2) % 13
                result.append(chr(beginning + ((ord(char) - beginning - shift) % 13)))
            else:
                result.append(char)
        elif char.isupper():
            if 'A' <= char <= 'M':
                beginning = ord('A')
                shift = shift1 % 13
                result.append(chr(beginning + ((ord(char) - beginning - shift) % 13)))
            elif 'N' <= char <= 'Z':
                beginning = ord('N')
                shift = (shift2 ** 2) % 13
                result.append(chr(beginning + ((ord(char) - beginning + shift) % 13)))
            else:
                result.append(char)
        else:
            result.append(char)
    return "".join(result)


def decrypt(text, shift1, shift2):
    result = []
    for char in text:
        if char.islower():
            if 'a' <= char <= 'm':
                beginning = ord('a')
                shift = (shift1 * shift2) % 13
                result.append(chr(beginning + ((ord(char) - beginning - shift) % 13)))
            elif 'n' <= char <= 'z':
                beginning = ord('n')
                shift = (shift1 + shift2) % 13
                result.append(chr(beginning + ((ord(char) - beginning + shift) % 13)))
            else:
                result.append(char)
        elif char.isupper():
            if 'A' <= char <= 'M':
                beginning = ord('A')
                shift = shift1 % 13
                result.append(chr(beginning + ((ord(char) - beginning + shift) % 13)))
            elif 'N' <= char <= 'Z':
                beginning = ord('N')
                shift = (shift2 ** 2) % 13
                result.append(chr(beginning + ((ord(char) - beginning - shift) % 13)))
            else:
                result.append(char)
        else:
            result.append(char)
    return "".join(result)


def encryption_function(shift1, shift2):
    with open("raw_text.txt", "r", encoding="utf-8") as f:
        original_text = f.read()
    encrypted_text = encrypt(original_text, shift1, shift2)
    with open("encrypted_text.txt", "w", encoding="utf-8") as f:
        f.write(encrypted_text)
    print("Encryption Successful. Encrypted file saved (encrypted_text.txt)")


def decryption_function(shift1, shift2):
    with open("encrypted_text.txt", "r", encoding="utf-8") as f:
        encrypted_text = f.read()
    decrypted_text = decrypt(encrypted_text, shift1, shift2)
    with open("decrypted_text.txt", "w", encoding="utf-8") as f:
        f.write(decrypted_text)
    with open("raw_text.txt", "r", encoding="utf-8") as f:
        original_text = f.read()
    with open("decrypted_text.txt", "r", encoding="utf-8") as f:
        decrypted_text = f.read()
    if decrypted_text == original_text:
        print("✅ Decryption successful. Decrypted file saved (decrypted_text.txt)")
    else:
        print("❌ Decryption failed! Incorrect shift values entered.")




if __name__ == "__main__":
    while True:    
        print("Choose an option:")
        print("1. Encrypt raw_text.txt")
        print("2. Decrypt encrypted_text.txt")
        print("3. Exit")
        choice = input("Welcome to Encryption Master 2000. Please enter 1, 2, or 3: ").strip()

        if choice in ("1", "2"):
            shift1 = int(input("Enter shift1: "))
            shift2 = int(input("Enter shift2: "))

        if choice == "1":
            encryption_function(shift1, shift2)
        elif choice == "2":
            decryption_function(shift1, shift2)
        elif choice == "3":
                print("Thank you for using Encryption Master 2000. Have a spectacular day! 🌈 ")
                break


        else:
            print("Ooft. Invalid option entered. Please try again.")