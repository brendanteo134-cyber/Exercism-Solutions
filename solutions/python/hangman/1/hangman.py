STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"
MAX_GUESSES = 9
class Hangman(object):
    def __init__(self, word):
        self.remaining_guesses = MAX_GUESSES
        self.__hidden_base_word = word
        self.guessed = set()
    def guess(self, char):
        if char in self.__hidden_base_word and char not in self.guessed:
            self.guessed.add(char)
            return
        if self.get_status() != STATUS_ONGOING:
            raise ValueError('The game has already ended.')
        self.remaining_guesses -= 1
    def get_masked_word(self):
        return ''.join(
            ch if ch in self.guessed else '_'
            for ch in self.__hidden_base_word
        )
    def get_status(self):
        if '_' not in self.get_masked_word():
            return STATUS_WIN
        if self.remaining_guesses < 0:
            return STATUS_LOSE
        return STATUS_ONGOING