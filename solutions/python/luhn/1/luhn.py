import re
class Luhn:
    def __init__(self, card_num):
        self.card_num = re.sub(' ','',card_num)
    def valid(self):
        card_num = self.card_num
        if len(card_num) <= 1 or not all(i.isnumeric() for i in card_num):
            return False
        res = [int(i) for i in card_num]
        res[-2::-2] = [2*i - 9*(i>=5) for i in res[-2::-2]]
        return not (sum(res)%10)
        