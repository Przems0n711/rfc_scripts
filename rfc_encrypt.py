def rfc_encryption(plain_text, key):
    plain_text = plain_text.replace(" ", "").upper()

    rows = key
    cols = len(plain_text)
    rfc = [['\n' for i in range(cols)] for j in range(rows)]

    direction = -1
    row = 0
    col = 0
    for i in range(cols):
        if row == 0 or row == rows-1:
            direction = -direction
        rfc[row][col] = plain_text[i]
        row += direction
        col += 1

    cipher_text = ""
    for i in range(rows):
        for j in range(cols):
            if rfc[i][j] != '\n':
                cipher_text += rfc[i][j]

    return cipher_text

plain_text = "Przemo loves Techni"
key = 2
cipher_text = rfc_encryption(plain_text, key)
print(f'The encrypted text is {cipher_text}')