import math

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
M = len(ALPHABET)

def encode(plain_text: str, a: int, b: int) -> str:
   
    if math.gcd(a, M) != 1:
        raise ValueError("a and m must be coprime.")
        
    encoded_chars = []
    for char in plain_text.lower():
        if char.isalpha():
            # E(x) = (a * x + b) mod m
            x = ALPHABET.index(char)
            encoded_index = (a * x + b) % M
            encoded_chars.append(ALPHABET[encoded_index])
        elif char.isdigit():
            encoded_chars.append(char)
            
 
    chunked = [
        "".join(encoded_chars[i:i + 5]) 
        for i in range(0, len(encoded_chars), 5)
    ]
    return " ".join(chunked)


def decode(cipherED_text: str, a: int, b: int) -> str:
   
    if math.gcd(a, M) != 1:
        raise ValueError("a and m must be coprime.")
        
  
    a_inv = pow(a, -1, M)
    
    decoded_chars = []
    for char in cipherED_text.lower():
        if char.isalpha():
            
            y = ALPHABET.index(char)
            decoded_index = (a_inv * (y - b)) % M
            decoded_chars.append(ALPHABET[decoded_index])
        elif char.isdigit():
            decoded_chars.append(char)
            
    return "".join(decoded_chars)