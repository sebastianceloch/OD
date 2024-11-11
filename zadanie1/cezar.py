def ceaser_cipher(text, key, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        key = 26 - key
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) + key - 97) % 26 + 97)
            else:
                result += chr((ord(char) + key - 65) % 26 + 65)
        else:
            result += char
    return result

text = "Hello world"
key = 3

encrypted_text = ceaser_cipher(text, key)
print(encrypted_text)
decrypted_text = ceaser_cipher(encrypted_text, key, 'decrypt')
print(decrypted_text)

