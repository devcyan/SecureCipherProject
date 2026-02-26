def caesar_cipher(text, shift=3, decrypt=False):
    result = ""
    shift = -shift if decrypt else shift
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr(((ord(char.lower()) - 97 + shift_amount) % 26) + 97)  # Fixed syntax
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char
    return result