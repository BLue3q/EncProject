import string
# English character frequencies
eng_freq = {
    'A': 8.167, 'B': 1.492, 'C': 2.782, 'D': 4.253, 'E': 12.702, 'F': 2.228,
    'G': 2.015, 'H': 6.094, 'I': 6.966, 'J': 0.153, 'K': 0.772, 'L': 4.025,
    'M': 2.406, 'N': 6.749, 'O': 7.507, 'P': 1.929, 'Q': 0.095, 'R': 5.987,
    'S': 6.327, 'T': 9.056, 'U': 2.758, 'V': 0.978, 'W': 2.360, 'X': 0.150,
    'Y': 1.974, 'Z': 0.074
}

def remove_duplicates(string):
    return ''.join(char for i, char in enumerate(string) if string.index(char) == i)

def create_matrix(key):
    key = remove_duplicates(key.replace(" ", "").upper())
    matrix = []
    for e in key:
        if e not in matrix:
            matrix.append(e)

    alphabet = "abcdefghiklmnopqrstuvwxyz"
    for e in alphabet:
        if e not in matrix:
            matrix.append(e)

    return [matrix[i:i+5] for i in range(0, 25, 5)]

def locate(char, matrix):
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if char == col:
                return i, j

def decrypt(cipher, key):
    matrix = create_matrix(key)
    plain_text = ""
    cipher = cipher.upper().replace(" ", "")
    for i in range(0, len(cipher), 2):
        char1, char2 = cipher[i], cipher[i+1]
        if char1 == char2:
            char1, char2 = 'X' + char2, char2 + 'X'
        pos1 = locate(char1, matrix)
        pos2 = locate(char2, matrix)
        if pos1 is None or pos2 is None:
            plain_text += char1 + char2  # Skip decryption if char not found
        else:
            row1, col1 = pos1
            row2, col2 = pos2
            if row1 == row2:
                plain_text += matrix[row1][(col1 - 1) % 5] + matrix[row1][(col2 - 1) % 5]
            elif col1 == col2:
                plain_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:
                plain_text += matrix[row1][col2] + matrix[row2][col1]
    return plain_text

def compute_char_freq(text):
    freq = {}
    for char in text.upper():
        if char in string.ascii_uppercase:
            freq[char] = freq.get(char, 0) + 1
    total = sum(freq.values())
    for char in freq:
        freq[char] = (freq[char] / total) * 100
    return freq


with open("cipher.txt", "r") as file:
    cipher_text = file.read().strip()

with open("key.txt", "r") as file:
    key = file.read().strip()


# Decrypt the ciphertext
plain_text = decrypt(cipher_text, key)
print(f"Decrypted text: {plain_text.lower()}")

cipher_freq = compute_char_freq(cipher_text)
plain_freq = compute_char_freq(plain_text)

print("\nCiphertext character frequencies:")
for char, freq in sorted(cipher_freq.items()):
    print(f"{char}: {freq:.2f}%")

print("\nPlaintext character frequencies:")
for char, freq in sorted(plain_freq.items()):
    print(f"{char}: {freq:.2f}%")

print("\nEnglish language character frequencies:")
for char, freq in sorted(eng_freq.items()):
    print(f"{char}: {freq:.3f}%")
