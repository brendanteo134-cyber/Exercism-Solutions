import string
import random
class Cipher:
    def __init__(self, key=None):
        self.letters = string.ascii_lowercase
        if key == None:
            self.key = ''.join(random.choices(self.letters, k=100))
        else:
            self.key = key.lower()
    def encode(self, text):
        coded_text = ''
        for idx, let in enumerate(text):
            text_letter_index = self.letters.find(let)
            key_letter_index = self.letters.find(self.key[idx % len(self.key)])
            coded_text = coded_text + self.letters[(text_letter_index + key_letter_index) % len(self.letters)]
        return coded_text
            
    def decode(self, text):
        decoded_text = ''
        for idx, let in enumerate(text):
           text_letter_index = self.letters.find(let)
           key_letter_index = self.letters.find(self.key[idx % len(self.key)])
           decoded_text = decoded_text + self.letters[(text_letter_index - key_letter_index) % len(self.letters)]
        return decoded_text