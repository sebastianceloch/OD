from collections import Counter
#czestotliwosc wystepowania liter w jezyku angielskim
frequency = [
    'e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z'
]
#szyfr cezara z 1 zadania
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

def frequency_analysis(text):
    text = text.lower()
    letter_counts = Counter(filter(str.isalpha, text)) # liczymy ilość wystąpień liter
    sorted_letters = [letter for letter, _ in letter_counts.most_common()] # sortujemy litery po ilości wystąpień
    return sorted_letters

def score_decryption(decrypted_text):
    decrypted_freq = frequency_analysis(decrypted_text)
    #obliczamy wynik dla rozkladu czestotliwosci liter w tekscie zaszyfrowanym i w jezyku angielskim
    #mniejszy wynik = lepsze dopasowanie do jezyka angielskiego
    score = sum(
        abs(frequency.index(letter) - decrypted_freq.index(letter))
        for letter in decrypted_freq if letter in frequency
    )
    return score

def decrypt_caesar(ciphertext, top_n=10):
    possible_decryptions = []
    for shift in range(26):
        #dla kazdego przesuniecia obliczamy wynik dopasowania do jezyka angielskiego
        decrypted_text = ceaser_cipher(ciphertext, shift, 'decrypt')
        score = score_decryption(decrypted_text)
        possible_decryptions.append((score, shift, decrypted_text))
    #sortujemy wyniki po score od najmniejszego czyli od najlepszego dopasowania
    possible_decryptions.sort()
    #zwracamy top_n najlepszych dopasowan
    return possible_decryptions[:top_n]

text = 'I thought witchers carried 2 swords, a steel one for humans and a silver one for monsters.'
ciphertext = ceaser_cipher(text, 8)
print(ciphertext)
possible_decryptions = decrypt_caesar(ciphertext)
for score, shift, decrypted_text in possible_decryptions:
    print(f"Shift: {shift}, Score: {score}, Decrypted text: {decrypted_text}")
    