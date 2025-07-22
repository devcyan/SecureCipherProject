def vigenere_encrypt(plaintext, keyword):
    encrypted = ""
    keyword = keyword.upper().replace(" ", "")
    key_idx = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(keyword[key_idx % len(keyword)]) - 65
            encrypted_char = chr((ord(char.upper()) - 65 + shift) % 26 + 65)
            encrypted += encrypted_char if char.isupper() else encrypted_char.lower()
            key_idx += 1
        else:
            encrypted += char
    return encrypted

def vigenere_decrypt(ciphertext, keyword):
    decrypted = ""
    keyword = keyword.upper().replace(" ", "")
    key_idx = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(keyword[key_idx % len(keyword)]) - 65
            decrypted_char = chr((ord(char.upper()) - 65 - shift) % 26 + 65)
            decrypted += decrypted_char if char.isupper() else decrypted_char.lower()
            key_idx += 1
        else:
            decrypted += char
    return decrypted