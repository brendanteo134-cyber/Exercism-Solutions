class BowlingGame:
    def __init__(self):
        self.rolled = []
        self.fin = None
        self.frame = frame()
        next(self.frame)
    def roll(self, pines):
        if not 10 >= pines >= 0:
            raise ValueError(f"Invalid pines number: {pines}")
        self.fin = self.frame.send(pines)
        self.rolled.append(pines)
    def score(self):
        if not self.fin:
            raise IndexError("More balls required")
        total = i = 0
        for _ in range(10):
            s = sum(self.rolled[i:i + 2])
            if 10 in (self.rolled[i], s):
                s += self.rolled[i + 2]
            total += s
            i = i + (1 if self.rolled[i] == 10 else 2)
        return total
def frame():
    for i in range(10):
        first = yield
        if first == 10:
            continue
        second = yield
        if first + second > 10:
            raise ValueError("Wrong number of pines in frame")
    if first == 10:
        a = yield
        b = yield
        if a + b > 10 and a != 10:
            raise ValueError("wrong number of pines in frame")
    elif first + second == 10:
        yield
    yield True
    raise IndexError("End of game")