from string import ascii_lowercase, ascii_uppercase, punctuation, whitespace

def encode(plain_text):
    string = decode(plain_text)
    return ' '.join([string[i:i+5] for i in range(0, len(string), 5)])

def decode(ciphered_text):
    mintext = ciphered_text.translate(str.maketrans('', '', \
        punctuation + whitespace))
    table = str.maketrans(ascii_lowercase + ascii_uppercase, \
        2 * ascii_lowercase[-1::-1])
    return mintext.translate(table)
