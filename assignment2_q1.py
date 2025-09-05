def encrypt(text, shift1, shift2):
    result = []
    for char in text:
        if char.islower():
            if 'a' <= char <= 'm':
                shift = shift1 * shift2
                result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
            elif 'n' <= char <= 'z':
                shift = shift1 + shift2
                result.append(chr((ord(char) - ord('a') - shift) % 26 + ord('a')))
            else:
                result.append(char)
        elif char.isupper():
            if 'A' <= char <= 'M':
                shift = shift1
                result.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
            elif 'N' <= char <= 'Z':
                shift = shift2 ** 2
                result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
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
                shift = shift1 * shift2
                result.append(chr((ord(char) - ord('a') - shift) % 26 + ord('a')))
            elif 'n' <= char <= 'z':
                shift = shift1 + shift2
                result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
            else:
                result.append(char)
        elif char.isupper():
            if 'A' <= char <= 'M':
                shift = shift1
                result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
            elif 'N' <= char <= 'Z':
                shift = shift2 ** 2
                result.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
            else:
                result.append(char)
        else:
            result.append(char)
    return "".join(result)


if __name__ == "__main__":
    shift1 = int(input("Enter shift1: "))
    shift2 = int(input("Enter shift2: "))

    with open("raw_text.txt", "r") as f:
        original_text = f.read()

    encrypted_text = encrypt(original_text, shift1, shift2)
    with open("encrypted_text.txt", "w") as f:
        f.write(encrypted_text)

    decrypted_text = decrypt(encrypted_text, shift1, shift2)
    with open("decrypted_text.txt", "w") as f:
        f.write(decrypted_text)

    if decrypted_text == original_text:
        print("✅ Decryption successful! Matches original.")
    else:
        print("❌ Decryption failed! Does not match original.")
