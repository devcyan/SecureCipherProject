def playfair_encrypt(plaintext, keyword):
    # Playfair matrix generation
    keyword = keyword.upper().replace("J", "I").replace(" ", "")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = []
    for char in keyword + alphabet:
        if char not in key:
            key.append(char)
    matrix = [key[i:i+5] for i in range(0, 25, 5)]
    
    # Prepare plaintext
    plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
    pairs = []
    i = 0
    while i < len(plaintext):
        if i == len(plaintext) - 1 or plaintext[i] == plaintext[i+1]:
            pairs.append(plaintext[i] + 'X')
            i += 1
        else:
            pairs.append(plaintext[i] + plaintext[i+1])
            i += 2
    
    # Encrypt pairs
    encrypted = ""
    for pair in pairs:
        row1, col1 = None, None
        row2, col2 = None, None
        for i, row in enumerate(matrix):
            if pair[0] in row:
                row1, col1 = i, row.index(pair[0])
            if pair[1] in row:
                row2, col2 = i, row.index(pair[1])
        if row1 == row2:
            encrypted += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            encrypted += matrix[row1][col2] + matrix[row2][col1]
    return encrypted

def playfair_decrypt(ciphertext, keyword):
    # Similar to encrypt but reverse the shifts
    keyword = keyword.upper().replace("J", "I").replace(" ", "")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = []
    for char in keyword + alphabet:
        if char not in key:
            key.append(char)
    matrix = [key[i:i+5] for i in range(0, 25, 5)]
    
    ciphertext = ciphertext.upper().replace(" ", "")
    pairs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    
    decrypted = ""
    for pair in pairs:
        row1, col1 = None, None
        row2, col2 = None, None
        for i, row in enumerate(matrix):
            if pair[0] in row:
                row1, col1 = i, row.index(pair[0])
            if pair[1] in row:
                row2, col2 = i, row.index(pair[1])
        if row1 == row2:
            decrypted += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            decrypted += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            decrypted += matrix[row1][col2] + matrix[row2][col1]
    return decrypted.replace("X", "")