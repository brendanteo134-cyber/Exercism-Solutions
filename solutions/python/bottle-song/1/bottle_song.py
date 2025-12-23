NUM_TO_TEXT = ["no", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
def recite(start, take=1):
    lines = []
    for num in range(start, start - take, -1):
        if num < start:
            lines.append("")
        lines += couplet(num)
    return lines
def couplet(start: int) -> list[str]:
    begin = line(start, initial=True)
    middle = "And if one green bottle should accidentally fall,"
    end = line(start - 1, initial=False)
    return [begin, begin, middle, end]
def line(number: int, initial: bool = False) -> str:
    text = NUM_TO_TEXT[number]
    bottles = f"bottle{'s' if number != 1 else ''}"
    if initial:
        return f"{text.title()} green {bottles} hanging on the wall,"
    else:
        return f"There'll be {text} green {bottles} hanging on the wall."