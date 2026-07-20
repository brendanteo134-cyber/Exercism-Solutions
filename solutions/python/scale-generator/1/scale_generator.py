SHARP_PITCHES = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
FLAT_PITCHES = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
SHARP_TONICS = [
    "C",
    "G",
    "D",
    "A",
    "E",
    "B",
    "F#",
    "a",
    "e",
    "b",
    "f#",
    "c#",
    "g#",
    "d#",
]
FLAT_TONICS = ["F", "Bb", "Eb", "Ab", "Db", "Gb", "d", "g", "c", "f", "bb", "eb"]
INTERVALS = {"m": 1, "M": 2, "A": 3}
def validate_interval_steps(intervals: str):
    return all(char in INTERVALS for char in intervals)
def validate_intervals_length(intervals: str):
    return len(intervals) <= 8
def get_pitches(tonic: str):
    if tonic in SHARP_TONICS:
        return SHARP_PITCHES
    elif tonic in FLAT_TONICS:
        return FLAT_PITCHES
    return None
class Scale:
    def __init__(self, tonic: str):
        self.tonic = tonic
        self.tonic_capitalized = tonic.capitalize()
        self.pitches = get_pitches(self.tonic)
    def chromatic(self):
        tonic_idx = self.pitches.index(self.tonic_capitalized)
        return self.pitches[tonic_idx:] + self.pitches[:tonic_idx]
    def interval(self, intervals: str):
        if not validate_interval_steps(intervals):
            raise ValueError('The supported intervals are "m", "M" and "A"')
        elif not validate_intervals_length(intervals):
            raise ValueError("Maximum number of intervals is 8")
        else:
            
            scale = self.chromatic() + [self.tonic_capitalized]
            curr_idx = 0
            result = [self.tonic_capitalized]
            print(scale)
            for interval in intervals:
                curr_idx += INTERVALS[interval]
                result.append(scale[curr_idx])
            return result