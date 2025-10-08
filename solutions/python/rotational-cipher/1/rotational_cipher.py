def rotate(text, key):
    newtext = ""
    for c in text:
        if c.isalpha():
            if c.isupper():
                newtext += chr(((ord(c) - 65 + key) %26) + 65) ## 65 == ord('A')
            else:
                newtext += chr(((ord(c) - 97 + key) %26) + 97) ## 97 == ord('a')
        else:
            newtext += c
    return newtext