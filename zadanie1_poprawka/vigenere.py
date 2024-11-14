def vigenere_cipher(text, key, mode='encrypt'):
    result = ""
    key = key.lower()
    key_length = len(key)
    key_index = 0

    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            shift = ord(key[key_index % key_length]) - 97

            if mode == 'decrypt':
                shift = -shift
            
            result += chr((ord(char) - offset + shift) % 26 + offset)
            key_index += 1
        else:
            result += char
    
    return result

text = input("Podaj tekst do zaszyfrowania/odszyfrowania: ")
key = input("Podaj klucz (tekstowy): ")
mode = input("Podaj tryb (encrypt/decrypt): ")

result_text = vigenere_cipher(text, key, mode)
print(result_text)