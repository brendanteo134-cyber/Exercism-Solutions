resistors = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}
metric_prefix = {1000000000: "giga", 1000000: "mega", 1000: "kilo"}
def label(colors):
    res = [resistors[v] for v in colors]
    resistance = int(f"{res[0]}{res[1]}")
    magnitude = int(f"{resistance}{'0'*res[2]}")
    suffix = "ohms"
    for base, prefix in metric_prefix.items():
        if magnitude >= base:
            suffix = f"{prefix}{suffix}"
            magnitude = int(magnitude / base)
            break
    return f"{magnitude} {suffix}"
