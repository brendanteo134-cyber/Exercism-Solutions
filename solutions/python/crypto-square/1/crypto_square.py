from re import sub
from math import sqrt, ceil
def cipher_text(plain_text):
    if not plain_text:
        return plain_text
    return code(plain_text)
def code(text):
    normalized = sub(r'[^a-z0-9]', '', text.lower())
    length = len(normalized)
    if length <= 1:
        return normalized
    c = ceil(sqrt(length)) # number of columns
    r = ceil(length / c)
    normalized += ' ' * (c*r - length)
    transpose = [normalized[i::c] for i in range(c)]
    return ' '.join(transpose)
