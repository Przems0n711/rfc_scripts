def rfc_decryption(cipher_text, key):
    cipher_text = cipher_text.upper()
    rows = key
    cols = len(cipher_text)
    rfc = [['\n' for i in range(cols)] for j in range(rows)]

    direction = -1
    row = 0
    col = 0
    for i in range(cols):
        if row == 0 or row == rows - 1:
            direction = -direction
        rfc[row][col] = '*'
        row += direction
        col += 1

    index = 0
    for i in range(rows):
        for j in range(cols):
            if rfc[i][j] == '*' and index < len(cipher_text):
                rfc[i][j] = cipher_text[index]
                index += 1

    plain_text = ""
    row = 0
    col = 0
    direction = -1
    for i in range(cols):
        if row == 0 or row == rows - 1:
            direction = -direction
        plain_text += rfc[row][col]
        row += direction
        col += 1

    return plain_text

cipher_text = "PZMLVSEHIREOOETCN"
key = 2
plain_text = rfc_decryption(cipher_text, key)
print(f'The decrypted text is {plain_text}')