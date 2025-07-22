def substitution_cipher(text, decrypt=False):
    substitution_key = {
        'a': 'q', 'b': 'w', 'c': 'e', 'd': 'r', 'e': 't', 'f': 'y', 'g': 'u',
        'h': 'i', 'i': 'o', 'j': 'p', 'k': 'a', 'l': 's', 'm': 'd', 'n': 'f',
        'o': 'g', 'p': 'h', 'q': 'j', 'r': 'k', 's': 'l', 't': 'z', 'u': 'x',
        'v': 'c', 'w': 'v', 'x': 'b', 'y': 'n', 'z': 'm'
    }
    if decrypt:
        reverse_key = {v: k for k, v in substitution_key.items()}
        return ''.join([reverse_key.get(char, char) for char in text])
    else:
        return ''.join([substitution_key.get(char, char) for char in text])