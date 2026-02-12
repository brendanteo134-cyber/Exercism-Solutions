RESISTOR_COLORS = (
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
)
RESISTOR_COLORS_TOLERANCE = {
    "silver": "10%",
    "gold": "5%",
    "red": "2%",
    "brown": "1%",
    "green": "0.5%",
    "blue": "0.25%",
    "violet": "0.1%",
    "grey": "0.05%",
}
def value(color):
    return RESISTOR_COLORS.index(color)
def resistor_label(colors):
    tolerance_color = colors[-1]
    if len(colors) == 4:
        resistance_value = (
            10 * value(colors[0]) + value(colors[1])
        ) * 10 ** value(colors[2])
    elif len(colors) == 5:
        resistance_value = (
            100 * value(colors[0]) + 10 * value(colors[1]) + value(colors[2])
        ) * 10 ** value(colors[3])
    else:
        return "0 ohms"
    prefix = ""
    if resistance_value >= 1_000_000_000:
        resistance_value /= 1_000_000_000
        prefix = "giga"
    elif resistance_value >= 1_000_000:
        resistance_value /= 1_000_000
        prefix = "mega"
    elif resistance_value >= 1_000:
        resistance_value /= 1_000
        prefix = "kilo"
    return (
        f"{resistance_value:g} "
        f"{prefix}ohms "
        f"±{RESISTOR_COLORS_TOLERANCE[tolerance_color]}"
    )
