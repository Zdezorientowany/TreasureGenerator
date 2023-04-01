
colors = {
    "copper": (255, 127, 0),
    "silver": (192, 192, 192),
    "gold": (255, 189, 27),
    "broken": (128, 128, 128),
    "good": (255, 255, 0),
    "flawless": (255, 165, 0),
    "jeweled": (160, 32, 240),
    "main": (0, 59, 79)
}

def format_text(text, color):
    r, g, b = colors[color]
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"