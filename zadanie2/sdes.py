def permute(input_bits, table):
    return [input_bits[i - 1] for i in table]

def left_shift(bits, shifts):
    return bits[shifts:] + bits[:shifts]

def xor(bits1, bits2):
    return [b1 ^ b2 for b1, b2 in zip(bits1, bits2)]

def sbox(input_bits, sbox_table):
    row = int(f"{input_bits[0]}{input_bits[3]}", 2)
    col = int(f"{input_bits[1]}{input_bits[2]}", 2)
    value = sbox_table[row][col]
    return [value >> 1, value & 1]

def fk(bits, subkey):
    left, right = bits[:4], bits[4:]
    expanded = permute(right, EP)
    xored = xor(expanded, subkey)
    sbox_result = sbox(xored[:4], S0) + sbox(xored[4:], S1)
    permuted = permute(sbox_result, P4)
    return xor(left, permuted) + right

def generate_keys(key):
    permuted_key = permute(key, P10)
    left, right = permuted_key[:5], permuted_key[5:]
    left = left_shift(left, 1)
    right = left_shift(right, 1)
    subkey1 = permute(left + right, P8)

    left = left_shift(left, 2)
    right = left_shift(right, 2)
    subkey2 = permute(left + right, P8)
    return subkey1, subkey2

def encrypt(plaintext, subkey1, subkey2):
    permuted = permute(plaintext, IP)
    result = fk(permuted, subkey1)
    swapped = result[4:] + result[:4]
    result = fk(swapped, subkey2)
    return permute(result, IP_INVERSE)

def decrypt(ciphertext, subkey1, subkey2):
    permuted = permute(ciphertext, IP)
    result = fk(permuted, subkey2)
    swapped = result[4:] + result[:4]
    result = fk(swapped, subkey1)
    return permute(result, IP_INVERSE)

P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8 = [6, 3, 7, 4, 8, 5, 10, 9]
IP = [2, 6, 3, 1, 4, 8, 5, 7]
IP_INVERSE = [4, 1, 3, 5, 7, 2, 8, 6]
EP = [4, 1, 2, 3, 2, 3, 4, 1]
P4 = [2, 4, 3, 1]

S0 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2]
]

S1 = [
    [0, 1, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3]
]

key = [1, 1, 0, 1, 1, 1, 0, 1, 0, 0]
plaintext = [1, 0, 1, 0, 1, 0, 0, 1]

subkey1, subkey2 = generate_keys(key)
print(f"Klucz 1: {''.join(map(str, subkey1))}")
print(f"Klucz 2: {''.join(map(str, subkey2))}")

ciphertext = encrypt(plaintext, subkey1, subkey2)
print(f"Zaszyfrowany tekst: {''.join(map(str, ciphertext))}")

decrypted = decrypt(ciphertext, subkey1, subkey2)
print(f"Odszyfrowany tekst: {''.join(map(str, decrypted))}")
