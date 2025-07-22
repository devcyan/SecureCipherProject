def rail_fence_encrypt(text, rails=3):
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    for char in text:
        fence[rail].append(char)
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction *= -1
    return ''.join([''.join(row) for row in fence])

def rail_fence_decrypt(ciphertext, rails=3):
    fence = [[] for _ in range(rails)]
    rail_lengths = [0] * rails
    idx = 0
    direction = 1
    for _ in ciphertext:
        rail_lengths[idx] += 1
        idx += direction
        if idx == rails - 1 or idx == 0:
            direction *= -1
    ptr = 0
    for i in range(rails):
        fence[i] = list(ciphertext[ptr:ptr + rail_lengths[i]])
        ptr += rail_lengths[i]
    decrypted = []
    rail = 0
    direction = 1
    for _ in range(len(ciphertext)):
        decrypted.append(fence[rail].pop(0))
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction *= -1
    return ''.join(decrypted)