def xor_encrypt(text, key):
    """
    Encrypts the input text using XOR cipher.
    :param text: Input text (plaintext or ciphertext).
    :param key: Integer key (0-255).
    :return: Encrypted/decrypted text.
    """
    encrypted = ""
    for char in text:
        encrypted += chr(ord(char) ^ key)  # XOR operation
    return encrypted

def xor_decrypt(ciphertext, key):
    """
    Decrypts the input ciphertext using XOR cipher.
    XOR encryption and decryption are the same operation.
    :param ciphertext: Encrypted text.
    :param key: Integer key (0-255).
    :return: Decrypted text.
    """
    return xor_encrypt(ciphertext, key)  # XOR is symmetric