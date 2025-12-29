class Clock:
    def __init__(self, hour, minute):
        self.hour = hour + minute // 60
        self.hour %= 24
        self.minute = minute % 60
    def __repr__(self):
        return f'Clock({self.hour}, {self.minute})'
    def __str__(self):
        return f'{self.hour:02d}:{self.minute:02d}'
    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute
    def __add__(self, minutes):
        m = self.minute + minutes
        h = self.hour + m // 60
        return Clock(h % 24, m % 60)
    def __sub__(self, minutes):
        m = self.minute - minutes
        h = self.hour
        if (m < 0):
            h -= abs(m // 60)
        return Clock(h % 24, m % 60)
